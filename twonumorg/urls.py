from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from django.contrib.sitemaps.views import index, sitemap
from allauth.account.decorators import secure_admin_login

from doublefloat.sitemaps import DoubleFloatSitemap
from projects.sitemaps import ProjectsSitemap

admin.site.site_header = f"twonum.org administration"
admin.site.site_title = f"Administration – twonum.org"  # En dash

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

sitemaps = {
    "doublefloat": DoubleFloatSitemap,
    "projects": ProjectsSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path("comments/", include('django_comments_xtd.urls')),
    path("_tz_detect/", include("tz_detect.urls")),
    path("avatar/", include("avatar.urls")),
    path("accounts/", include("allauth.urls")),
    path("_martor/", include("martor.urls")),
    # Sitemaps
    path('sitemap.xml', index, {'sitemaps': sitemaps}),
    path('sitemap.xml/<section>.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    # twonum.org
    path("doublefloat/", include("doublefloat.urls")),
    path("projects/", include("projects.urls")),
    path("about/", include("about.urls")),
    path("", include("home.urls")),
]

# Handle media files in development
# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )

# Custom error pages
handler404 = "core.views.error_404"
handler500 = "core.views.error_500"
