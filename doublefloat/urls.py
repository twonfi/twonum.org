from django.urls import path

from doublefloat import views
from doublefloat.feeds import DoubleFloatRSSFeed, DoubleFloatAtomFeed

app_name = "doublefloat"

urlpatterns = [
    path("posts/<slug:slug>/", views.view_post, name="view_post"),
    path("categories/<slug:slug>/", views.category, name="category"),
    path("feed.rss", DoubleFloatRSSFeed(), name="rss_feed"),
    path("feed.atom", DoubleFloatAtomFeed(), name="atom_feed"),
    path("", views.home, name="home"),
]
