from django.urls import path
from glory.views import *

urlpatterns = [
    path('', index, name='index')
]