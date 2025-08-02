from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed, Atom1Feed
from minify_html import minify

from .models import Project
from core.templatetags.markdown_extras import sanitized_markdown


# noinspection PyMethodMayBeStatic
class ProjectsFeed(Feed):
    title = "twonum's projects"
    link = "/projects/"  # To avoid circular import with reverse()
    description = "Projects made by twonum"

    def items(self):
        return Project.objects.order_by("-date")

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return minify(sanitized_markdown(item.desc))

    def item_author_name(self, item):
        return item.author

    def item_pubdate(self, item):
        return item.date


class ProjectsRSSFeed(ProjectsFeed):
    feed_type = Rss201rev2Feed


class ProjectsAtomFeed(ProjectsFeed):
    feed_type = Atom1Feed
