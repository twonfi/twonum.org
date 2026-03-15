from django.contrib import admin

from projects import models

admin.site.register((models.Project,))
