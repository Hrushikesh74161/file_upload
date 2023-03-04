from pathlib import Path
import csv

from django.views.generic import FormView, ListView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from django.utils.decorators import method_decorator

from accounts.decorators import login_required
from file_handler.forms import UploadForm
from file_handler.utils import (
    get_file_path,
    file_exists,
    get_rows_from_csv_file,
    get_rows_from_xlsx_file,
)


class FileUploadView(FormView):
    template_name = "file_handler/home.html"
    form_class = UploadForm
    success_url = reverse_lazy("file_handler:home")

    def form_valid(self, form):
        file = self.request.FILES["file"]
        path: Path = get_file_path(file, force=True)
        with open(path, "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)
        messages.success(
            self.request, message=f"File {path.name} uploaded successfully."
        )
        return redirect(self.success_url)


class FileView(ListView):
    template_name = 'file_handler/file_view.html'
    paginate_by = 15
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'file_name': self.kwargs.get('file_name'),
        })
        return context

    def get_queryset(self):
        file_name = self.kwargs.get('file_name')
        file_type = file_name.split(".")[-1]

        if file_type in settings.ACCEPTED_FILES and file_exists(file_name):
            path = str(get_file_path(file_name=file_name))
            data = []
            if file_type == "csv":
                data = get_rows_from_csv_file(path)
            elif file_type == "xlsx":
                data = get_rows_from_xlsx_file(path)

            return data
        else:
            raise Exception(f'File not in {settings.ACCEPTED_FILES}')
        

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

