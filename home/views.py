from django.shortcuts import render
from django.db.models import Model
from django.utils.csp import CSP
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
INDEX_CSP["default-src"] += [
    "https://pagering.gideon.sh/flower.png",
]
INDEX_CSP["frame-src"] += [
    "https://webring.hackclub.com/embed.html",
    "https://pagering.gideon.sh/embed/",
]
INDEX_CSP["style-src"] = [
    CSP.SELF,
    CSP.UNSAFE_INLINE,
    "https://pagering.gideon.sh/embed/",
] + settings.CORS_ALLOWED_ORIGINS
INDEX_CSP["script-src"] = INDEX_CSP["style-src"]
INDEX_CSP["font-src"] += [
    "data:",
]
INDEX_CSP["connect-src"] += [
    "https://pagering.gideon.sh/embed/",
    "https://pagering.gideon.sh/api/",
]


@csp_override(config=INDEX_CSP)
def index(request):
    context = {
        "title": "twonum's website",
        "show_site_name_in_title": False,
        "h1_from_title": False,
        "buttons": Button.objects.filter(
            featured_sortkey__isnull=False
        ).order_by("featured_sortkey"),
    }

    return render(request, "home/index.html", context)
