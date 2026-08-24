from django.db import models
from django.core.validators import DomainNameValidator

from home.models import Button


class Link(models.Model):
    """A link between worlds."""

    domain = models.CharField(
        unique=True,
        max_length=255,
        verbose_name="Domain name",
        validators=[DomainNameValidator()],
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Website name",
    )

    def __str__(self) -> str:
        return self.domain


class PersonalWebsite(Link):
    """A link to another personal website."""

    button = models.OneToOneField(
        Button,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The website's 88x31 button.",
    )
