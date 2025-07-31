from django.contrib import admin

from .models import TimeMachine

admin.site.register([
    TimeMachine,
])
