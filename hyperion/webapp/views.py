from django.http import HttpResponse
from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")