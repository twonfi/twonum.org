from django.shortcuts import render
from django.db.models import Model
from django.views.decorators.csp import csp_override
from django.conf import settings

from home.models import Button


def _latest_or_none(model: type[Model], *args):
    try:
        m = model.objects.latest(*args)
    except model.DoesNotExist:
        return None
    else:
        return m

INDEX_CSP = settings.SECURE_CSP
INDEX_CSP["frame-src"] = INDEX_CSP["frame-src"] + [
    "https://webring.hackclub.com/embed.html"
]


@csp_override(config=INDEX_CSP)
def index(request):
    context = {
        "title": "twonum's website",
        "show_site_name_in_title": False,
        "h1_from_title": False,
        "buttons": Button.objects.all().order_by("id"),
    }

    return render(request, "home/index.html", context)
