from django.urls import path

from .views import *

app_name = "doublefloat"

urlpatterns = [
    path("<slug:slug>/", view_post, name="view_post"),
    path("", home, name="home"),
]
