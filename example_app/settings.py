"""
Django settings for example_app project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Uncomment for Grappelli
    "grappelli",
    # Uncomment for Jazzmin
    # "jazzmin",
    # Uncomment for Admin Interface
    # "admin_interface",
    # "colorfield",
    # Uncomment for Jest
    # "jet.dashboard",
    # "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",  # Need for Auth messages
    "django.contrib.staticfiles",
    "django.contrib.sites",  # Optional: Add Sites framework
    "django_google_sso",  # Add django_google_sso
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "example_app.urls"

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

WSGI_APPLICATION = "example_app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

if "jet" in INSTALLED_APPS:
    # Jet Theme
    JET_DEFAULT_THEME = "light-gray"

    JET_THEMES = [
        {
            "theme": "default",  # theme folder name
            "color": "#47bac1",  # color of the theme's button in user menu
            "title": "Default",  # theme title
        },
        {"theme": "green", "color": "#44b78b", "title": "Green"},
        {"theme": "light-green", "color": "#2faa60", "title": "Light Green"},
        {"theme": "light-violet", "color": "#a464c4", "title": "Light Violet"},
        {"theme": "light-blue", "color": "#5EADDE", "title": "Light Blue"},
        {"theme": "light-gray", "color": "#222", "title": "Light Gray"},
    ]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = ["backend.MyBackend"]

# Uncomment GOOGLE_SSO_CALLBACK_DOMAIN to use Sites Framework site domain
# Or comment both and use domain retrieved from accounts/login/ request
SITE_ID = 1
GOOGLE_SSO_CALLBACK_DOMAIN = os.getenv("GOOGLE_SSO_CALLBACK_DOMAIN")

GOOGLE_SSO_SESSION_COOKIE_AGE = 3600  # default value
GOOGLE_SSO_CLIENT_ID = os.getenv("GOOGLE_SSO_CLIENT_ID")
GOOGLE_SSO_PROJECT_ID = os.getenv("GOOGLE_SSO_PROJECT_ID")
GOOGLE_SSO_CLIENT_SECRET = os.getenv("GOOGLE_SSO_CLIENT_SECRET")

GOOGLE_SSO_ALLOWABLE_DOMAINS = os.getenv("GOOGLE_SSO_ALLOWABLE_DOMAINS", "").split(",")
GOOGLE_SSO_AUTO_CREATE_FIRST_SUPERUSER = (
    False  # Mark as True, to create superuser on first eligible user login
)
GOOGLE_SSO_STAFF_LIST = os.getenv("GOOGLE_SSO_STAFF_LIST", "").split(",")
GOOGLE_SSO_SUPERUSER_LIST = os.getenv("GOOGLE_SSO_SUPERUSER_LIST", "").split(",")
GOOGLE_SSO_TIMEOUT = 10  # default value
GOOGLE_SSO_SCOPES = [  # default values
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

# Optional: Add if you want to use custom authentication backend
GOOGLE_SSO_AUTHENTICATION_BACKEND = "backend.MyBackend"

# Optional: Add pre-login logic
# GOOGLE_SSO_PRE_LOGIN_CALLBACK = "backend.pre_login_callback"

# Uncomment to disable SSO login
# GOOGLE_SSO_ENABLED = False  # default: True

# Uncomment to disable user auto-creation
# GOOGLE_SSO_AUTO_CREATE_USERS = False  # default: True
