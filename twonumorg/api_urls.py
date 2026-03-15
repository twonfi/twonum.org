#  Copyright (C) 2026 twonum
#
#  twonum.org is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  twonum.org is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with twonum.org.  If not, see <https://www.gnu.org/licenses/>.
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from pronums.views import PronumViewSet
import core.views

app_name = "api"

rest_router = DefaultRouter()
rest_router.register("pronums", PronumViewSet, basename="pronum")
rest_router.register("users", core.views.UserViewSet, basename="user")

urlpatterns = [
    re_path(r"^(?P<version>(v\d+))/", include(rest_router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="api:schema"),
        name="redoc",
    ),
]
