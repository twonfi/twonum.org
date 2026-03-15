from django.db import models
from django.conf import settings
from django.urls import reverse
from martor.models import MartorField

from doublefloat.models import Category as DoubleFloatCategory

User = settings.AUTH_USER_MODEL


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = MartorField("Description")
    banner = models.ImageField(upload_to="project-banners")
    date = models.DateTimeField()

    demo_url = models.URLField("Demo URL")
    repo_url = models.URLField("Repository URL")

    doublefloat_category = models.OneToOneField(
        DoubleFloatCategory,
        on_delete=models.SET_NULL,
        related_name="doublefloat_category",
        blank=True,
        null=True,
    )

    allow_comments = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects:project_page", kwargs={"project_id": self.id})
