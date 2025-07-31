from django.db import models
from django.contrib.sites.models import Site


class TimeMachine(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE,
        primary_key=True)
    hits = models.PositiveBigIntegerField()
    allow_comments = True  # Guestbook uses django-comments-xtd

    def __str__(self):
        return str(self.site)
