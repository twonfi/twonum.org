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
