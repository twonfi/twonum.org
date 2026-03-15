from django.urls import path

from projects import views
from projects.feeds import ProjectsRSSFeed, ProjectsAtomFeed

app_name = "projects"

urlpatterns = [
    path("<int:project_id>/", views.project_page, name="project_page"),
    path("feed.rss", ProjectsRSSFeed(), name="rss_feed"),
    path("feed.atom", ProjectsAtomFeed(), name="atom_feed"),
    path("", views.home, name="home"),
]
