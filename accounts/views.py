import datetime
import os

from django.views.generic import FormView, ListView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.signing import Signer
from django.core.files import File

from accounts.auth import authenticate
from accounts.decorators import login_required
from accounts.forms import LoginForm
from file_handler.forms import UploadForm
from utils import signer


class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy("accounts:admin")
    template_name = "accounts/login.html"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        if authenticate(username, password):
            response = HttpResponseRedirect(self.success_url)
            cookie_value = signer.sign_object(f"{username};{password}")
            response.set_cookie(
                "auth",
                cookie_value,
                max_age=datetime.timedelta(days=1),
                secure=True,
                samesite="lax",
            )
            return response
        else:
            return HttpResponse("Invalid username or password.")


def logout(request: HttpRequest):
    response = HttpResponseRedirect(reverse("accounts:login"))
    response.delete_cookie("auth")
    return response


class AdminView(ListView):
    template_name = "accounts/admin.html"
    context_object_name = "files"
    paginate_by = 10

    def get_queryset(self):
        dir_path = settings.FILE_ROOT
        files = os.listdir(dir_path)
        # sorts the files based on their creation time, descending
        file_names = sorted(
            files,
            key=lambda f: os.path.getctime(os.path.join(settings.FILE_ROOT, f)),
            reverse=True,
        )
        files = []
        for name in file_names:
            file_path = "/media/files/" + name
            files.append({"name": name, "path": file_path})

        return files

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

