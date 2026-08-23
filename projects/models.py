from django.db import models
from django.conf import settings
from django.urls import reverse

from doublefloat.models import Category as DoubleFloatCategory

User = settings.AUTH_USER_MODEL


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.TextField("Description")
    banner = models.ImageField(upload_to="project-banners", null=True, blank=True)
    banner_alt = models.CharField(max_length=511, null=True, blank=True, verbose_name="Banner alt text")
    date = models.DateTimeField()

    demo_url = models.URLField("Demo URL", null=True, blank=True)
    repo_url = models.URLField("Repository URL", null=True, blank=True)

    doublefloat_category = models.OneToOneField(
        DoubleFloatCategory,
        on_delete=models.SET_NULL,
        related_name="doublefloat_category",
        blank=True,
        null=True,
    )

    allow_comments = False

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects:project_page", kwargs={"project_id": self.id})
