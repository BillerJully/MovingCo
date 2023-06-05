from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

"""redirect to home redirect('way', permanent = False)"""
def mainpage(request):
    return render(request, '')


def makeoreder(request):
    return render(request, '')


def aboutus(request):
    return render(request, '')


def job(request):
    return render(request, '')


def pageNotFound(request, exception):
    return render(request, '')


def clientfeedback(request):
    return render(request, '')


