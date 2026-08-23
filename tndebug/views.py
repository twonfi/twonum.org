from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.conf import settings

from tndebug.forms import DebugForm


def debug_form(request):
    if not settings.DEBUG:
        raise PermissionDenied

    form = DebugForm()

    context = {
        "title": "Debug form",
        "form": form,
    }

    return render(request, "debug/form.html", context)
