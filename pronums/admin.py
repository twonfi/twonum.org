from django.contrib import admin

from pronums import models

admin.site.register(
    [
        models.Pronum,
    ]
)
