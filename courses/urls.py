from django.urls import path
from .views import *

app_name = 'courses'
urlpatterns = [
    path('', index, name='index'),
]