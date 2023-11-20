from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello')


def first(request):
    return render(request, '1.html')


def second(request):
    return render(request, '2.html')
