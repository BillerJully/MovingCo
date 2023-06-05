from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', mainpage, name='home'),
    path('feedback/', clientfeedback),
    path('jobs/', job),
    path('aboutus/', aboutus),
    path('makeorder/', makeoreder)
]