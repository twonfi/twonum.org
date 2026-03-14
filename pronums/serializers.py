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
from rest_framework import serializers

from pronums.models import Pronum


class PronumSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name="api:user-detail",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Pronum
        fields = ["id", "author", "text", "quote", "date"]
        read_only_fields = ("id", "author", "date")
