from django.contrib.sitemaps import Sitemap

from .models import Post


# noinspection PyMethodMayBeStatic
class DoubleFloatSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return Post.objects.filter()

    def lastmod(self, item):
        return item.date

    def location(self, item):
        return item.get_absolute_url()
