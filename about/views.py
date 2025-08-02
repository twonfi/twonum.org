from django.shortcuts import render

from .models import TimeMachine
from projects.models import Project


def about(request):
    time_machine = TimeMachine.objects.get_or_create(site=request.site)[0]
    time_machine.hits += 1
    time_machine.save()

    context = {
        "title": "About me",
        "h1_from_title": False,
        "masonry": True,
        "time_machine": time_machine,
        "projects": Project.objects.all().order_by('-date')[:4],
    }

    return render(request, "about/about.html", context)
