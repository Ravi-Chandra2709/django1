from django.http import HttpResponse
from django.shortcuts import render
import operator
# Create your views here.
def home(requests):
    return render(requests,'wordcount/home.html', {'name' : 'ravi'})
def about(requests):
    return render(requests,'wordcount/about.html', {'userid' : 'raviuserid'})





