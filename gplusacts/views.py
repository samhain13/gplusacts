from django.http import HttpResponse
from django.template import Context, loader
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
    
    template = loader.get_template("gplusacts/index.html")
    context = Context({
        "activities": activities,
    })
    return HttpResponse(template.render(context))

