from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from gplusacts.models import Activity, Attachment

def index(request):
    # Check whether the settings prescribe a number of posts to show per page.
    psettings = 5
    if hasattr(settings, "GPLUSACTS_POSTS_PER_PAGE"):
        psettings = settings.GPLUSACTS_POSTS_PER_PAGE
    paginator = Paginator(Activity.objects.all(), psettings)
    # Get the page number, if any.
    page = request.GET.get("page")
    # Paginate.
    try:
        ap = paginator.page(page)
    except PageNotAnInteger:
        ap = paginator.page(1)
    except EmptyPage:
        ap = paginator.page(paginator.num_pages)
    # Build our context.
    context = {
        "activities": [],
        "current_page": ap.number,
        "total_pages": ap.paginator.num_pages,
        "has_previous": ap.has_previous,
        "has_next": ap.has_next,
        "previous_page_number": ap.previous_page_number,
        "next_page_number": ap.next_page_number,
    }
    # Populate our context's activities list with Google+ activities;
    # including their attachments, if any.
    for activity in ap:
        a = dict()
        a["activity"] = activity
        a["attachments"] = []
        for att in Attachment.objects.filter(activity=activity):
            a["attachments"].append(att)
        context["activities"].append(a)
    return render(request, "gplusacts/index.html", context)

