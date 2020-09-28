from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastre-se/', register, name='register'),
]