from django.db import models
from django.urls import reverse
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.text import slugify
from martor.models import MartorField

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    desc = MartorField("Description")
    slug = models.SlugField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('doublefloat:category',
            kwargs={"slug": self.slug})


class Post(models.Model):
    sites = models.ManyToManyField(Site, related_name="sites")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=255, unique=True)
    body = MartorField()
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name="favorites", blank=True)
    categories = models.ManyToManyField(Category,
        related_name="category", blank=True)
    allow_comments = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('doublefloat:view_post',
            kwargs={"slug": self.slug})
