from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def college(requests):
    return HttpResponse('<h2>Vasavi College of Engineering</h2>')

def year(requests):
    return HttpResponse('<h1> IIIrd year 1st sem </h1>')

