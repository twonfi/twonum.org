from pathlib import Path
import os

from django.conf.global_settings import SESSION_COOKIE_SECURE
from django.contrib.messages import constants as messages
from django.urls import reverse
from environ import Env
from csp import constants as csp

BASE_DIR = Path(__file__).resolve().parent.parent
env = Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    STATIC_ROOT=(str, ""),
    MEDIA_ROOT=(str, ""),
    SITE_ID=(int, 1),
    INSTALLED_APPS=(list, []),
    NOINDEX=(bool, True),
    # Email
    EMAIL_SMTP_HOST=(str, ""),
    EMAIL_SMTP_PORT=(int, 25),
    EMAIL_SMTP_HOST_USER=(str, ""),
    EMAIL_SMTP_HOST_PASSWORD=(str, ""),
    EMAIL_SMTP_USE_TLS=(bool, False),
    EMAIL_SMTP_USE_SSL=(bool, False),
    EMAIL_SMTP_SSL_CERTFILE=(str, None),
    EMAIL_SMTP_SSL_KEYFILE=(str, None),
    EMAIL_SMTP_TIMEOUT=(int, 3),
)
Env.read_env(os.path.join(BASE_DIR, ".env"))


def _env_file(key: str) -> str:
    env_ = env(key)

    if env_[:2] == './':
        return str(BASE_DIR / env_[2:])
    return str(Path(env_))


DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
# No excuse to not use HTTPS
CSRF_TRUSTED_ORIGINS = [f"https://{h}" for h in ALLOWED_HOSTS]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    "django.contrib.sitemaps",
    # Single-line stuff
    "whitenoise.runserver_nostatic",
    "tz_detect",
    "django_bootstrap5",
    "rest_framework",
    "martor",
    "avatar",
    # allauth
    "allauth_ui",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.mfa",
    "widget_tweaks",
    "slippers",
    "django_minify_html",
    # django-crispy-forms
    "crispy_forms",
    "crispy_bootstrap5",
    # Auto-delete files after change in the associated object
    "django_cleanup.apps.CleanupConfig",
    # django-comments-xtd (in this order!)
    "django_comments_xtd",
    "django_comments",
    # twonum.org
    "core",
    "doublefloat",
    "projects",
    "about",
    "home",
]
INSTALLED_APPS += env("INSTALLED_APPS")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    # From packages
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django_minify_html.middleware.MinifyHtmlMiddleware",
    "tz_detect.middleware.TimezoneMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "twonumorg.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "slippers.templatetags.slippers",
            ],
        },
    },
]

WSGI_APPLICATION = "twonumorg.wsgi.application"

# Email
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": env.db()
}


# Email
DEFAULT_FROM_EMAIL = env("EMAIL_FROM")
SERVER_EMAIL = env("EMAIL_FROM_SERVER")
match env("EMAIL_BACKEND"):
    case "smtp":
        EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
        EMAIL_HOST = env("EMAIL_SMTP_HOST")
        EMAIL_PORT = env("EMAIL_SMTP_PORT")
        EMAIL_HOST_USER = env("EMAIL_SMTP_HOST_USER")
        EMAIL_HOST_PASSWORD = env("EMAIL_SMTP_HOST_PASSWORD")
        EMAIL_USE_TLS = env("EMAIL_SMTP_USE_TLS")
        EMAIL_USE_SSL = env("EMAIL_SMTP_USE_SSL")
        EMAIL_SSL_CERTFILE = env("EMAIL_SMTP_SSL_CERTFILE")
        EMAIL_SSL_KEYFILE = env("EMAIL_SMTP_SSL_KEYFILE")
        EMAIL_TIMEOUT = env("EMAIL_SMTP_TIMEOUT")
    case "console":
        EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    case "dummy":
        EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
]


# CORS and CSP
CORS_ALLOWED_ORIGINS = [
    "https://cdn.jsdelivr.net",
    "https://cdnjs.cloudflare.com",
    "https://unpkg.com",
]
# CONTENT_SECURITY_POLICY = {
#     "DIRECTIVES": {
#         "default-src": [csp.SELF] + CORS_ALLOWED_ORIGINS,
#         "script-src": [csp.SELF, csp.NONCE] + CORS_ALLOWED_ORIGINS,
#         "style-src": [csp.SELF, csp.NONCE] + CORS_ALLOWED_ORIGINS,
#         "frame-ancestors": [csp.SELF],
#         "form-action": [csp.SELF],
#         "report-uri": "/csp-report/",
#     },
# }


# HTTPS stuff
if not DEBUG:
    CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE = True
    # SECURE_SSL_REDIRECT = True  # Issues with the Nest server?


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-ca"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and media files
# https://docs.djangoproject.com/en/5.2/howto/static-files/

if DEBUG:
    STATIC_URL = "static/"

    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"
else:
    STATIC_URL = env("STATIC_URL")
    STATIC_ROOT = _env_file("STATIC_ROOT")

    MEDIA_URL = env("MEDIA_URL")
    MEDIA_ROOT = _env_file("MEDIA_ROOT")

    STATICFILES_STORAGE = ('whitenoise.'
                           'storage.CompressedManifestStaticFilesStorage')

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Sites framework
SITE_ID = env("SITE_ID")

# NOINDEX
NOINDEX = env("NOINDEX")

# allauth
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
ACCOUNT_SIGNUP_FIELDS = ['username*', 'email*', 'password1*', 'password2*']
LOGIN_REDIRECT_URL = "/"
MFA_SUPPORTED_TYPES = ["totp", "webauthn", "recovery_codes"]
MFA_PASSKEY_LOGIN_ENABLED = True
MFA_PASSKEY_SIGNUP_ENABLED = True

if DEBUG:
    MFA_WEBAUTHN_ALLOW_INSECURE_ORIGIN = True

# Use Argon2 to hash passwords
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# django-crispy-forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Bootstrap message tags
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# martor
MARTOR_THEME = "bootstrap"
MARTOR_ENABLE_ADMIN_CSS = False
MARTOR_TOOLBAR_BUTTONS = [
    "bold",
    "italic",
    "horizontal",
    "heading",
    "pre-code",
    "blockquote",
    "unordered-list",
    "ordered-list",
    "link",
    "image-link",
    # 'emoji',  # until dependency hell with pymdownx is fixed
    "direct-mention",
    "toggle-maximize",
    "help",
]
MARTOR_ALTERNATIVE_JS_FILE_THEME = 'martor/martor.js'
MARTOR_ALTERNATIVE_CSS_FILE_THEME = 'martor/martor.css'

# django-comments-xtd
COMMENTS_APP = "django_comments_xtd"
COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': True,
        'who_can_post': 'all',
    },
}
COMMENTS_XTD_FROM_EMAIL = env("EMAIL_FROM")
COMMENTS_XTD_CONTACT_EMAIL = env("EMAIL_CONTACT")
# COMMENTS_XTD_API_GET_USER_AVATAR = "core.utils.avatar_url_from_comment"

# django-avatar
AVATAR_PROVIDERS = (
    "avatar.providers.PrimaryAvatarProvider",
    "avatar.providers.GravatarAvatarProvider",
)
AVATAR_GRAVATAR_DEFAULT = "identicon"
