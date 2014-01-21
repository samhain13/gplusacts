from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from gplusacts.models import Activity, Attachment


def index(request):
    return render(request, "index.html",
                  _build_context(request, _get_paginator(1)))

def page(request, pagenum):
    if pagenum == "1":
        return redirect(index)
    return render(request, "index.html",
                  _build_context(request, _get_paginator(int(pagenum))))

def _build_context(request, ap):
    # Build our context.
    context = {
        "activities": [],
        "acts_title": getattr(settings,
            "GPLUSACTS_TITLE", "My Google+ Activities"),
        "acts_description": getattr(settings,
            "GPLUSACTS_DESC", "My Google+ activities..."),
        "current_page": ap.number,
        "total_pages": ap.paginator.num_pages,
        "back": None,
        "next": None,
    }
    # See if we have a custom title.
    # We'll just create the back and next links here instead of on
    # the template because we have things that we have to decide on.
    path = [x for x in request.get_full_path().split("/")
            if x != "page" and x.isalpha()]
    path.insert(0, "")   # For making an absolute URI later.
    path.append("page")  # We know that the second-to-last component is "page".
    if ap.has_previous():
        context["back"] = "/".join(path + [repr(ap.previous_page_number())])
    if ap.has_next():
        context["next"] = "/".join(path + [repr(ap.next_page_number())])
    # Populate our context's activities list with Google+ activities;
    # including their attachments, if any.
    for activity in ap:
        a = dict()
        a["activity"] = activity
        a["attachments"] = []
        for att in Attachment.objects.filter(activity=activity):
            a["attachments"].append(att)
        context["activities"].append(a)
    return context

def _get_paginator(page):
    # Check whether the settings prescribe a number of posts to show per page.
    psettings = getattr(settings, "GPLUSACTS_POSTS_PER_PAGE", 5)
    paginator = Paginator(Activity.objects.all().order_by("-published"), psettings)
    # Paginate.
    try:
        ap = paginator.page(page)
    except PageNotAnInteger:
        ap = paginator.page(1)
    except EmptyPage:
        ap = paginator.page(paginator.num_pages)
    return ap

