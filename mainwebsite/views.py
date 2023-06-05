from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

"""redirect to home redirect('way', permanent = False)"""
def mainpage(request):
    return render(request, 'mainwebsite/mainpage.html')


def makeoreder(request):
    return render(request, 'mainwebsite/makeorder.html.html')


def aboutus(request):
    return render(request, 'mainwebsite/aboutus.html.html')


def job(request):
    return render(request, 'mainwebsite/job.html')


def clientfeedback(request):
    return render(request, 'mainwebsite/clientsfeedback.html')


def pageNotFound(request, exception):
    return render(request, 'mainwebsite/pageNotFound.html')



