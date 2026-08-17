from django.contrib import admin

from music import models

admin.site.register(
    (
        models.Artist,
        models.Release,
        models.Track,
    )
)
