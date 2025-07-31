from django import template
from markdown import markdown as md
from nh3 import clean
from strip_markdown import strip_markdown as strip_md

# from pymdownx.emoji import EmojiExtension, gemoji

# pymdownx temporarily disabled due to a dependency hell situation with
# Markdown versions conflicting with martor

register = template.Library()


@register.filter
def sanitized_markdown(text):
    return md(
        clean(text),
        extensions=[
            "markdown.extensions.fenced_code",
            "markdown.extensions.tables",
            # 'pymdownx.highlight',
            "codehilite",  # Temporary replacement
            # 'pymdownx.magiclink',
            # 'pymdownx.betterem',
            # 'pymdownx.tilde',
            # 'pymdownx.tasklist',
            # 'pymdownx.superfences',
            # 'pymdownx.saneheaders',
            # 'pymdownx.magiclink',
            # EmojiExtension(emoji_index=gemoji),
        ],
    )


@register.filter
def strip_markdown(text):
    return strip_md(text)
