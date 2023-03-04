from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('admin/', views.AdminView.as_view(), name='admin'),
]
