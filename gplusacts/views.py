from django.shortcuts import render
from gplusacts.models import Activity, Attachment

def index(request):
    activities = []
    for activity in Activity.objects.all():
        a = dict()
        a["activity"] = activity
        a["attachments"] = []
        for att in Attachment.objects.filter(activity=activity):
            a["attachments"].append(att)
        activities.append(a)
    context = {
        "activities": activities,
    }
    return render(request, "gplusacts/index.html", context)

