from django.urls import path

from .views import *
from .feeds import DoubleFloatRSSFeed, DoubleFloatAtomFeed

app_name = "doublefloat"

urlpatterns = [
    path("posts/<slug:slug>/", view_post, name="view_post"),
    path("categories/<slug:slug>/", category, name="category"),
    path("feed.rss", DoubleFloatRSSFeed(), name="rss_feed"),
    path("feed.atom", DoubleFloatAtomFeed(), name="atom_feed"),
    path("", home, name="home"),
]
