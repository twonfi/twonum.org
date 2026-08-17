from datetime import datetime

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

# from django.urls import reverse
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from twonumorg import BLOCKED_USER_AGENTS
from core import serializers

User = get_user_model()


def robots_txt(request):
    context = {
        "user_agents": BLOCKED_USER_AGENTS,
    }

    resp = render(request, "robots.txt", context)
    resp["Content-Type"] = "text/plain; charset=utf-8"
    return resp


# noinspection PyUnusedLocal
def error_401(request, message: str | None = None):
    """401 must be done manually."""
    context = {
        "exception": message,
    }
    resp = render(request, "core/errors/401.txt", context, status=401)
    resp["Content-Type"] = "text/plain; charset=utf-8"
    return resp


# noinspection PyUnusedLocal
def error_403(request, exception):
    context = {
        "exception": str(exception),
    }
    resp = render(request, "core/errors/403.txt", context, status=403)
    resp["Content-Type"] = "text/plain; charset=utf-8"
    return resp


# noinspection PyUnusedLocal
def error_404(request, exception):
    resp = render(request, "core/errors/404.txt", status=404)
    resp["Content-Type"] = "text/plain; charset=utf-8"
    resp["The-Truly-Evil-Devs"] = "Status: 404"
    return resp


# noinspection PyUnusedLocal
def error_500(request):
    resp = render(request, "core/errors/500.txt", status=500)
    resp["Content-Type"] = "text/plain; charset=utf-8"
    return resp


# noinspection PyUnusedLocal
def ping(request):
    data = {"date": datetime.now().isoformat(), "server": settings.SERVER}

    return JsonResponse(data)


def clankers_txt(request):
    resp = render(request, "clankers.txt")
    resp["Content-Type"] = "text/plain; charset=utf-8"
    return resp


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]
