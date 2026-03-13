from django.db import models
from django.conf import settings
from django.urls import reverse
from nh3 import clean

User = settings.AUTH_USER_MODEL


class Pronum(models.Model):
    """A pronum.

    Pronums are short thoughts (like tweets) that can be streamed to a
    user and are much simpler than DoubleFloat posts.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(
        help_text="This will be placed inside an HTML list item."
                  " Don't use HTML. Use quote for blockquote format."
    )
    quote = models.BooleanField(
        verbose_name="Show as quote",
        help_text="Whether to show this pronum as a blockquote"
    )
    date = models.DateTimeField(auto_now_add=True)

    allow_comments = False

    def __str__(self):
        return self.text

    def get_formatted_html(self):
        """Get sanitized HTML for the pronum depending on whether it is
        a quote.
        """
        text = clean(self.text, tags=set())

        if self.quote:
            return f"<blockquote><pre>{text}</pre></blockquote>"
        else:
            return text


    def get_absolute_url(self):
        return reverse("pronums:year", kwargs={
            "year": self.date.year,
        }) + f"#pronum-{self.id}"
