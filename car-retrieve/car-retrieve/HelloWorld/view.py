__author__ = 'BK'
from django.http import HttpResponse
from django.shortcuts import render



def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'demo.html', context)