from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', mainpage, name='home'),
    path('feedback/', clientfeedback, name='feedback'),
    path('jobs/', job, name='jobs'),
    path('aboutus/', aboutus, name='aboutus'),
    path('makeorder/', makeoreder, name='makeorder')
]