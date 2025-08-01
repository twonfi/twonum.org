from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sites.shortcuts import get_current_site
from django.db.utils import OperationalError
from django.views.i18n import JavaScriptCatalog
from allauth.account.decorators import secure_admin_login

try:
    site = get_current_site(None)
    admin.site.site_header = f"{site.name} administration"
    admin.site.site_title = f"{site.name} site admin"
except OperationalError:
    pass

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path("comments/", include('django_comments_xtd.urls')),
    path("_tz_detect/", include("tz_detect.urls")),
    path("avatar/", include("avatar.urls")),
    path("accounts/", include("allauth.urls")),
    path("_martor/", include("martor.urls")),
    # twonum.org
    path("posts/", include("doublefloat.urls")),
    path("projects/", include("projects.urls")),
    path("about/", include("about.urls")),
    path("", include("home.urls")),
]

# Handle media files in development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

