from pathlib import Path
from os import getenv, path
import dotenv
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

# SETTING UP DOT ENV FILE FOR LOCAL ENVIRONMENT
dotenv_file = BASE_DIR / ".env.local"
if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# SECRET KEY FOR CREDENTIALS
SECRET_KEY = getenv("DJANGO_SECRET_KEY", get_random_secret_key())

DEBUG = getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

CORS_ALLOWED_ORIGINS = getenv(
    "CORS_ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000"
).split(",")
CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "djoser",
    "social_django",
    "vault",
    "opinion",
    "tags",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "citadel.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "citadel.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# AUTHENTICATION

AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "vault.authentication.CustomJWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
}

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "reset-password/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "activation/{uid}/{token}",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "TOKEN_MODEL": None,
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": getenv("REDIRECT_URLS").split(","),
    "SERIALIZERS": {
        "current_user": "vault.serializers.CustomUserSerializer",
    },
}

AUTH_COOKIE = "access"
AUTH_COOKIE_MAX_AGE = 60 * 60 * 24
AUTH_COOKIE_SECURE = getenv("AUTH_COOKIE_SECURE", "True") == "True"
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = "/"
AUTH_COOKIE_SAMESITE = "None"

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = getenv("GOOGLE_AUTH_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = getenv("GOOGLE_AUTH_SECRET_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]

SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ["first_name", "last_name"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "vault.UserAccount"

# EMAIL SETTINGS
EMAIL_BACKEND = "django_ses.SESBackend"
AWS_SES_ACCESS_KEY_ID = getenv("AWS_SES_ACCESS_KEY_ID")
AWS_SES_SECRET_ACCESS_KEY = getenv("AWS_SES_SECRET_ACCESS_KEY")
AWS_SES_REGION_NAME = getenv("AWS_SES_REGION_NAME")
AWS_SES_REGION_ENDPOINT = f"email.{AWS_SES_REGION_NAME}.amazonaws.com"
AWS_SES_FROM_EMAIL = getenv("AWS_SES_FROM_EMAIL")
USE_SES_V2 = True

DEFAULT_FROM_EMAIL = getenv("AWS_SES_FROM_EMAIL")

# site details for email sending
DOMAIN = getenv("DOMAIN")
SITE_NAME = "Citadel"
