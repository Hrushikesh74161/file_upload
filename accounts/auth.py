from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.conf import settings


def authenticate(username, password):
    username_valid = (username == settings.ADMIN_USERNAME)
    pwd_valid = check_password(password, settings.ADMIN_PASSWORD)

    if username_valid and pwd_valid:
        return True
    else:
        return False
