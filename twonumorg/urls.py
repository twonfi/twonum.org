from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path("admin/", admin.site.urls),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path("comments/", include('django_comments_xtd.urls')),
    path("_tz_detect/", include("tz_detect.urls")),
    path("avatar/", include("avatar.urls")),
    path("accounts/", include("allauth.urls")),
    path("_martor/", include("martor.urls")),
    # twonum.org
    path("posts/", include("doublefloat.urls"))
]
