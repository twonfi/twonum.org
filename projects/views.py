from django.shortcuts import render, get_object_or_404

from .models import Project


def home(request):
    context = {
        "title": "My projects",
        "masonry": True,
        "projects": Project.objects.all(),
    }

    return render(request, "projects/home.html", context)


def project_page(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    context = {
        "title": project.name,
        "p": project,
    }

    return render(request, "projects/project_page.html", context)
