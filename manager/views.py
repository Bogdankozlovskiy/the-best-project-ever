from django.http import HttpResponse
from django.shortcuts import render


def hello(request, name="filipp", digit=None):
    if digit is not None:
        return HttpResponse(f"digit is {digit}")
    return HttpResponse(f"hello {name}")
# Create your views here.
