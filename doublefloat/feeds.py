from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed, Atom1Feed
from minify_html import minify

from .models import Post
from core.templatetags.markdown_extras import sanitized_markdown


# noinspection PyMethodMayBeStatic
class DoubleFloatFeed(Feed):
    title = "DoubleFloat"
    link = "/posts/"  # To avoid circular import with reverse()
    description = "The twonum blog"

    def items(self):
        return Post.objects.order_by("-date")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return minify(sanitized_markdown(item.body))

    def item_author_name(self, item):
        return item.author


class DoubleFloatRSSFeed(DoubleFloatFeed):
    feed_type = Rss201rev2Feed


class DoubleFloatAtomFeed(DoubleFloatRSSFeed):
    feed_type = Atom1Feed
