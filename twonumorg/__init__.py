"""twonum.org main plumbing."""

import ipware
from django.http import HttpRequest

# These user agents are disallowed in robots.txt and blocked by
# ``twonumorg.middleware.BlockUserAgentsMiddleware``.
BLOCKED_USER_AGENTS = (
    # AI training crawlers
    "Amazonbot",
    "Applebot-Extended",
    "Bytespider",
    "CCBot",
    "ClaudeBot",
    "anthropic-ai",
    "Google-Extended",
    "GoogleAgent-Mariner",
    "GPTBot",
    "OAI-SearchBot",
    "meta-externalagent",
    "PerplexityBot",
    "TikTokSpider",
    "Cohere",
    "MistralAI-User",
)


def get_client_ip(request: HttpRequest, *args, **kwargs):
    return ipware.get_client_ip(
        request, *args, proxy_trusted_ips=["127.0.0.1", "::1"], **kwargs
    )
