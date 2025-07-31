from django.shortcuts import render

from .models import TimeMachine


def about(request):
    time_machine = TimeMachine.objects.get_or_create(site=request.site)[0]
    time_machine.hits += 1
    time_machine.save()

    context = {
        "title": "About me",
        "h1_from_title": False,
        "time_machine": TimeMachine.objects.get(site=request.site)
    }

    return render(request, "about/about.html", context)
