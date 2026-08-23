from django.shortcuts import render

from .models import TimeMachine


def about(request):
    time_machine = TimeMachine.objects.get_or_create(site=request.site)[0]
    time_machine.hits += 1
    time_machine.save()

    context = {
        "title": "contact me",
        "time_machine": time_machine,
    }

    return render(request, "about/contact.html", context)
