from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def poll(request):
    return HttpResponse("Hello world. You're at the polls index.")