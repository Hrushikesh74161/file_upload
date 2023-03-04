from django.urls import path

from file_handler import views

app_name = 'file_handler'

urlpatterns = [
    path('', views.FileUploadView.as_view(), name='home'),
    path('files/<file_name>', views.FileView.as_view(), name='file_view'),
]
