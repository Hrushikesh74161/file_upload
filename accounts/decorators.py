from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.core.signing import Signer
from django.conf import settings

from accounts.auth import authenticate
from utils import signer


def login_required(func):
    def wrapper(request: HttpRequest, *args, **kwargs):
        auth = request.COOKIES.get('auth', None)
        if auth is not None:
            auth = signer.unsign_object(auth)
            if authenticate(*auth.split(';')):
                return func(request, *args, **kwargs)

        return redirect('accounts:login')

    return wrapper