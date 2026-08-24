from django.shortcuts import render

from cityfolk.models import PersonalWebsite


def folks(request):
    personal_websites = PersonalWebsite.objects.all().order_by("name")

    context = {
        "title": "folks and buddies",
        "personal_websites": personal_websites,
    }

    return render(request, "cityfolk/folks.html", context)
