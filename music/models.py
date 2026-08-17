from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator
from django.utils._os import safe_join
from django.utils.crypto import get_random_string

# Example:
# https://resonantunion.bandcamp.com/album/chicory-a-musical-tale

subdomain_validator = RegexValidator(
    regex=r"^[a-z0-9][a-z0-9-]+[a-z0-9]",
    message="Must be a valid subdomain.",
    code="invalid_subdomain",
)


class Artist(models.Model):
    """An artist."""

    # "resonant-union"
    slug = models.SlugField(primary_key=True, max_length=32)
    # "Resonant Union"
    name = models.CharField(max_length=245)
    # ""               # Automatically filled in
    sort_key = models.CharField(max_length=255, null=True, blank=True)

    # "resonantunion"  # https://resonantunion.bandcamp.com
    bandcamp_subdomain = models.CharField(max_length=255, null=True, blank=True, help_text="If the artist uses Bandcamp, otherwise leave blank", validators=[subdomain_validator])

    # uuid.UUID("1fcfc89e-d830-4050-b99e-715350011177")
    musicbrainz = models.UUIDField(null=True, blank=True, verbose_name="MusicBrainz ID")

    # None             # Not notable for Wikipedia yet
    wikipedia_title = models.CharField(max_length=255, null=True, blank=True, help_text="Should use underscores instead of spaces and be a valid MediaWiki title")

    # Images, etc. are left out intentionally.
    # They cannot be formatted well.  Copyright is also hard to manage.

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.sort_key:
            self.sort_key = self.name

        super().save(*args, **kwargs)


def get_cover_filename(instance: Release, filename: str) -> str:
    ext = filename.split('.')[-1]
    if instance.slug:
        filename = f"{instance.slug}_{get_random_string(12)}.{ext}"
    else:
        filename = f"{get_random_string(18)}.{ext}"
    return f"music-covers/{filename}"


class Release(models.Model):
    """A release, either an album or a single."""

    # "chicory-a-musical-tale"
    slug = models.SlugField(primary_key=True, max_length=32)
    # "Chicory: A Musical Tale"
    title = models.CharField(max_length=255)
    # False
    single = models.BooleanField(default=False, help_text="Whether the track is a single. Doesn't make a difference except for labels.")
    # <Artist: "resonant-union">
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True, help_text="Leave blank for various artists")
    # [300x300 PNG file]
    # Yes, MusicBrainz has full-resolution covers,
    # but tn.o is not MusicBrainz.
    # Insert all-your-friends-jumping-off-a-bridge-type saying here.
    cover = models.ImageField(null=True, blank=True, upload_to=get_cover_filename, help_text='Full-resolution covers should not be uploaded except in some rare cases (Lena Raine\'s "PhantomaOS", CC BY-SA, or Gayle\'s "abcdefu", public domain) due to copyright. Use ImageMagick to resize to 300x300. Move to TheCrypt, paste into File Explorer: magick cover.png -resize 300x300 cover.png')
    # "This album is great because ..."
    notes = models.TextField(null=True, blank=True)

    # True
    bandcamp = models.BooleanField(verbose_name="On Bandcamp")
    # "resonantunion"             # //resonantunion.bandcamp.com/[...]
    bandcamp_subdomain = models.CharField(null=True, blank=True, help_text="Must be used with Bandcamp slug.", validators=[subdomain_validator])
    # "chicory-a-musical-tale"    # //[...]/album/chicory-a-musical-tale
    bandcamp_slug = models.SlugField(null=True, blank=True, help_text="Must be used with Bandcamp subdomain.")
    # 4257906981
    bandcamp_id = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Bandcamp album ID", help_text="For embed player. On Bandcamp, click Embed, the wordpress.com, and find album=[...]. Fully optional.")

    # uuid.UUID("73812318-b820-4189-9460-b802fd7fec6a")
    musicbrainz = models.UUIDField(null=True, blank=True, verbose_name="MusicBrainz ID")

    def __str__(self) -> str:
        return self.title

    def clean(self) -> None:
        super().clean()

        if (
            self.bandcamp
            # self.bandcamp_id is excluded here.
            # The template checks for the ID to show the embed player.
            and (not self.bandcamp_subdomain and not self.bandcamp_slug)
        ):
            msg = 'Subdomain and slug must be set if "On Bandcamp".'
            raise ValidationError({
                "bandcamp": msg,
                "bandcamp_subdomain": msg,
                "bandcamp_slug": msg,
            })


class Track(models.Model):
    """A track, similar to a MusicBrainz "Recording"."""

    # <Release: "chicory-a-musical-tale">
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    # 2
    number = models.PositiveIntegerField()
    # "The Colorful World We Left Behind"
    title = models.CharField(max_length=255)

    # Feature creep: tn.o is not trying to become a MusicBrainz.
    # Other details should be left out.

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["release", "number"], name="unique_release_track")
        ]

    def __str__(self) -> str:
        return self.title
