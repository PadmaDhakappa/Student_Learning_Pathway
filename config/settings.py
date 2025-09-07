"""
Django settings for config project (Render-ready).
"""

from pathlib import Path
import os

# Optional: read local .env for development; on Render you set env vars in the dashboard
try:
    from dotenv import load_dotenv  # pip install python-dotenv
    load_dotenv()
except Exception:
    pass

import dj_database_url  # pip install dj-database-url

# -------------------------------------------------------------------
# Paths & basics
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "dev-insecure-key")  # set on Render > Environment
DEBUG = os.getenv("DEBUG", "False") == "True"

# Accept Render host by default; you can lock this down later
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# Django 5 defaults
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -------------------------------------------------------------------
# Installed apps
# -------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # Make WhiteNoise serve static files even when using runserver (dev convenience)
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    # Third-party
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    # Your apps
    "api",
]

# -------------------------------------------------------------------
# Middleware (order matters)
# -------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Serve static files efficiently on Render
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # CORS must be high in the stack, before CommonMiddleware
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# -------------------------------------------------------------------
# Templates
# -------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # add BASE_DIR / "templates" if you create a templates folder
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------------------------------------------------------------------
# Database
# On Render: attach a Postgres instance, which provides DATABASE_URL.
# Locally: falls back to SQLite.
# -------------------------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=True,
    )
}

# -------------------------------------------------------------------
# Static files (admin CSS/JS) – served by WhiteNoise on Render
# -------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -------------------------------------------------------------------
# Security / proxy settings for Render
# -------------------------------------------------------------------
# Trust Render's proxy so request.is_secure() works and HTTPS is respected
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

# CSRF & hosts for Render domains; add your frontend origin when you have it.
CSRF_TRUSTED_ORIGINS = list(
    filter(
        None,
        set(
            [
                "https://*.onrender.com",
                "https://*.render.com",
                # You can add more origins via env var, comma separated
                *os.getenv("CSRF_TRUSTED_EXTRA", "").split(","),
            ]
        ),
    )
)

# -------------------------------------------------------------------
# Django REST Framework & schema
# -------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 25,
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
}

SPECTACULAR_SETTINGS = {
    "TITLE": "School Read-only API",
    "DESCRIPTION": "Read-only endpoints for school data",
    "VERSION": "1.0.0",
}

# -------------------------------------------------------------------
# CORS (open for now; lock to your frontend domain when you know it)
# To restrict, set CORS_ALLOWED_ORIGINS env var with comma-separated URLs.
# -------------------------------------------------------------------
_cors_from_env = [o for o in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if o]
if _cors_from_env:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = _cors_from_env
else:
    CORS_ALLOW_ALL_ORIGINS = True

# -------------------------------------------------------------------
# Logging to stdout (handy on Render)
# -------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}
