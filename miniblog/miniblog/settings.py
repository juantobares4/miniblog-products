"""
Django settings for miniblog project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-lm_-3$o_n%#2#zsfnkjszh4@#rb+7@br29ohd0i*#+gggra_3s"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django_filters",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "product",
    "home",
    "users",
    "api_v1",

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

ROOT_URLCONF = "miniblog.urls"

import os

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Tenemos que agregar todos los context processor que tengamos a settings.
                "miniblog.context_processors.all_names_products",
                "miniblog.context_processors.all_names_categories",
                "miniblog.context_processors.profile_language"

            ],

        },

    },

]

WSGI_APPLICATION = "miniblog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
from django.utils.translation import gettext_lazy as _ 

LANGUAGE_CODE = "es" # Lenguaje por defecto del sistema

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Español')),


)

TIME_ZONE = "UTC" 

USE_I18N = True
USE_L10N = True
USE_TZ = True

import os

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),

)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/" 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # BASE_DIR es donde está el manage.py

"""import sentry_sdk

sentry_sdk.init( # Puede ir en cualquier lado del archivo settings.py
    dsn="https://c01571c75f4812c7e7282e90f512db71@o4507817866887168.ingest.us.sentry.io/4507860992851968",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
"""
""" LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {modulo} {message}',
            'style': '{',

        },

        'simple':{
            'verbose': {
            'format': '{levelname} {message}',
            'style': '{',

        },
        }

    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter' : 'simple'

        },

        'sentry': {
            'level': 'ERROR',
            'class': 'sentry_sdk.integrations.logging.EventHandler',

        }

    },

    'loggers': {
        'django':{
            'handlers': ['console', 'sentry'],
            'level': 'DEBUG'

        },

        'custom': {
            'handlers': ['console', 'sentry'],
            'level': 'CRITICAL'

        }
    }

} """ 

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'api_v1.paginations.Pagination',
    'PAGE_SIZE': 100 # Limite de resultados mostrados. 

}

# SMTP es un protocolo.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '4b8cdd199e02d9'
EMAIL_HOST_PASSWORD = '39db643402076d'
EMAIL_PORT = '2525'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@itec.com' 