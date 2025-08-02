from django.urls import path

from .views import *
from .feeds import ProjectsRSSFeed, ProjectsAtomFeed

app_name = "projects"

urlpatterns = [
    path("<int:project_id>/", project_page, name="project_page"),
    path("feed.rss", ProjectsRSSFeed(), name="rss_feed"),
    path("feed.atom", ProjectsAtomFeed(), name="atom_feed"),
    path("", home, name="home"),
]
