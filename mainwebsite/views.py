from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
from .models import *
"""redirect to home redirect('way', permanent = False)"""

websitemenu = [ {'title': 'Main page',  'url_name': 'home'},
                {'title': 'Make order', 'url_name': 'makeorder'},
                {'title': 'Our clients', 'url_name': 'feedback'},
                {'title': 'Jobs', 'url_name': 'jobs'},
                {'title': 'About us', 'url_name': 'aboutus'}]


def mainpage(request):
    context = {'menu': websitemenu,
               'Title': 'Main page'}
    return render(request, 'mainwebsite/mainpage.html', context=context )


def makeoreder(request):
    context = {'menu': websitemenu,
               'Title': 'Order page'}
    return render(request, 'mainwebsite/makeorder.html', context=context)


def aboutus(request):
    context = {'menu': websitemenu,
               'Title': 'About us'}
    return render(request, 'mainwebsite/aboutus.html', context=context)


def job(request):
    context = {'menu': websitemenu,
               'Title': 'Jobs'}
    return render(request, 'mainwebsite/job.html', context=context)


def clientfeedback(request):
    feedback = Clientsfeedback.objects.all()
    context = {'feedback': feedback,
               'menu': websitemenu,
               'Title': 'Feedback'}
    return render(request, 'mainwebsite/clientsfeedback.html', context=context)


def pageNotFound(request, exception):
    context = {'menu': websitemenu,
               'Title': 'PageNotFound'}
    return render(request, 'mainwebsite/pageNotFound.html', )



