from django.urls import path

from tndebug import views

app_name = "tndebug"

urlpatterns = [
    path("form/", views.debug_form),
]
