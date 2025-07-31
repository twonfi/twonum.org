from django.urls import path

from .views import *

app_name = "projects"

urlpatterns = [
    path("<int:project_id>/", project_page, name="project_page"),
    path("", home, name="home"),
]
