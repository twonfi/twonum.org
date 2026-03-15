from django.contrib import admin

from doublefloat import models

admin.site.register(
    (
        models.Category,
        models.Post,
    )
)
