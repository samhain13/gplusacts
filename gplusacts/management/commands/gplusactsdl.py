import json
import urllib2

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import utc
from datetime import datetime

from gplusacts.models import Activity, Attachment

help_text = """Downloads a Google+ feed and saves the activities into this
app's database. This command was designed to be run with Cron, as in:

/path/to/python /path/to/./manage.py gplusactsdl <profile_id> <api_key>

Where:
    profile_id, Google+ profile ID
    api_key, Google+ API key
"""

gpurl = "https://www.googleapis.com/plus/v1/people/%s/activities/public?key=%s"
tstrf = "%Y-%m-%dT%H:%M:%S.%fZ"


class Command(BaseCommand):
    args = ""
    help = help_text
    
    def handle(self, *args, **kargs):
        # We want two arguments.
        if len(args) != 2:
            raise CommandError("must have 2 arguments, see help for details.")
        activities = self._get_json(args[0], args[1])
        # We want a dict.
        if type(activities) != dict:
            raise TypeError("server returned something that wasn't JSON.")
        for a in activities.get("items", []):
            self._save_activity(a)
    
    def _get_json(self, gplusid, apikey):
        """Downloads the JSON from the Google+ server."""
        try:
            u = urllib2.urlopen(gpurl % (gplusid, apikey))
            return json.loads(u.read())
        except:
            # If this fails for anything, just return a dict with an empty list.
            return {"items": []}
    
    def _save_activity(self, a):
        """Maps an activity item into the app's Activity model."""
        # Ensure that we have no duplicates. We can find that out by checking
        # the publication date since we can't have two that are alike.
        try:
            published = datetime.strptime(a.get("published"),
                tstrf).replace(tzinfo=utc)
        except:
            published = datetime.now().replace(tzinfo=utc)
        if len(Activity.objects.filter(published=published)) == 0:
            obj = Activity()
            obj.objtype = a["object"].get("objectType", "")
            obj.content = a["object"].get("content", "")
            obj.url = a.get("url", "")
            obj.published = published
            # Save the object now because attachments will need an existing
            # object for establishing the foreign key relationship.
            obj.save()
            # Get the attachments.
            for att in a["object"].get("attachments", []):
                self._save_attachment(att, obj)
    
    def _save_attachment(self, attachment, activity):
        """Maps an attachment item into the app's Attachment model."""
        att = Attachment()
        att.objtype = attachment.get("objectType", "")
        att.title = attachment.get("displayName", "")
        att.content = attachment.get("content", "")
        att.url = attachment.get("url", "")
        if attachment.has_key("image"):
            att.image = attachment["image"]["url"]
        # Create the relationship between the activity and this attachment.
        att.activity = activity
        att.save()

