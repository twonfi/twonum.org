from django.urls import path

from cityfolk import views

app_name = "cityfolk"

urlpatterns = [
    path("", views.folks, name="folks"),
]
