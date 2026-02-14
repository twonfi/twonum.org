import re

from django.http import HttpResponse

from twonumorg import BLOCKED_USER_AGENTS


class BlockUserAgentsMiddleware:
    """Block access to twonum.org for user agents blocked in
    ``twonumorg.BLOCKED_USER_AGENTS``.

    A few pages are allowed, such as robots.txt and .well-known pages.
    All other pages return a 403 if accessed by a crawler.
    """

    HTTP_RESPONSE_TEXT = r"""403: Forbidden.
       ______
      /      \
      | SLOP |
      \______/
         ||
         ||>-(twonum)

<> ---------------------------------------------------------- <>

This crawler is not allowed to access twonum.org.
Please obey robots.txt.

All crawlers used to collect data for AI training and similar
AI processes may not crawl twonum.org.

<> ---------------------------------------------------------- <>

If you're a human who is seeing this, please contact me using a
method on hub.twonum.org.

<> ---------------------------------------------------------- <>

© twonum.
Licensed under the GNU Affero General Public License, version 3
and Creative Commons Attribution-ShareAlike 4.0 International.
There is absolutely no warranty.
"""
    ALLOWED_PATH_REGEX = re.compile(r"^/(?:robots.txt|\.well-known/.*)$")

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

        if (
            user_agent
            and any(ua.lower() in user_agent for ua in BLOCKED_USER_AGENTS)
            and not self.ALLOWED_PATH_REGEX.search(request.path)
        ):
            resp = HttpResponse(self.HTTP_RESPONSE_TEXT, status=400)
            resp["Content-Type"] = "text/plain; charset=utf-8"
            return resp

        return self.get_response(request)
