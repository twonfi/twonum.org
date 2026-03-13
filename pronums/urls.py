from django.urls import path

from pronums import views

app_name = "pronums"

urlpatterns = [
    path("<int:year>/", views.year_view, name="year"),
    path("", views.home, name="home"),
]
