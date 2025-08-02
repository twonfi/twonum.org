from django.contrib.sitemaps import Sitemap

from .models import Project


# noinspection PyMethodMayBeStatic
class ProjectsSitemap(Sitemap):
    def items(self):
        return Project.objects.filter()

    def lastmod(self, item):
        return item.date

    def location(self, item):
        return item.get_absolute_url()
