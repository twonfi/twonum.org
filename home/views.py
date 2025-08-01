from django.shortcuts import render

from projects.models import Project
from doublefloat.models import Post


def home(request):
    context = {
        "title": "twonum.org",
        "show_site_name_in_title": False,
        # "h1_from_title": False,
        "post": Post.objects.latest("date"),
        "project": Project.objects.latest("id"),
        "user_agent": request.headers.get("User-Agent"),
        "project_count": Project.objects.count(),
    }

    return render(request, "home/home.html", context)
