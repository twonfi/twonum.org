from django.shortcuts import render
from django.db.models import Model

from projects.models import Project
from doublefloat.models import Post


def _latest_or_none(model: type[Model], *args):
    try:
        m = model.objects.latest(*args)
    except model.DoesNotExist:
        return None
    else:
        return m


def home(request):
    context = {
        "title": "twonum.org",
        "show_site_name_in_title": False,
        # "h1_from_title": False,
        "post": _latest_or_none(Post, "date"),
        "project": _latest_or_none(Project, "id"),
        "user_agent": request.headers.get("User-Agent"),
        "project_count": Project.objects.count(),
    }

    return render(request, "home/home.html", context)
