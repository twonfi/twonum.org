from django.db import models
from django.utils.crypto import get_random_string


def get_button_filename(instance: Button, filename: str) -> str:
    ext = filename.split(".")[-1]
    if instance.name:
        filename = f"{instance.name}_{get_random_string(12)}.{ext}"
    else:
        filename = f"{get_random_string(18)}.{ext}"
    return f"buttons/{filename}"


class Button(models.Model):
    """An 88x31 button."""

    name = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to=get_button_filename,
        help_text="Should be a PNG file, not a GIF or JPEG file. Especially not a WebP file.",
    )
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    alt = models.CharField(
        max_length=511,
        verbose_name="Alt text",
        help_text="Required. Read by screen readers. Describe the image itself.",
    )
    title = models.CharField(
        max_length=511,
        blank=True,
        null=True,
        help_text='Also known as the "hover text", also read by screen readers.',
    )
    featured_sortkey = models.PositiveIntegerField(
        verbose_name="Sort key on home page",
        blank=True,
        null=True,
        help_text="Add a number to add to home page. Sorted ascending.",
    )

    def __str__(self) -> str:
        return self.name
