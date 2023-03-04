from pathlib import Path
import os
import datetime
import random

CHOICES = 'abcdefghijklmnopqrstuvxyz0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ'

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-&35hwj7e_p_qpy#vv^i#5pfy_8!pca5z%gd%%($aq%ggeq&-4i"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'file_handler',
    'accounts',
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

ROOT_URLCONF = "file_upload.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "file_upload.wsgi.application"

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

USE_TZ = True

STATIC_URL = "static/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = 'media/'

FILE_ROOT = os.path.join(MEDIA_ROOT, 'files')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ADMIN_USERNAME = 'admin'

ADMIN_PASSWORD = 'pbkdf2_sha256$390000$fwO7fpPiqYrMtcPDosk8PX$tbFVK3hM//g5/Ik7BHoHcEtgXpH6LzzQWV+RZFMEpSQ='

HASH_SALT = SECRET_KEY

ACCEPTED_FILES = ["csv", "xlsx", "xls"]

