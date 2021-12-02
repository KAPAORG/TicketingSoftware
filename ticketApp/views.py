from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect

# Create your views here.

def index(request):
    return render(request, 'base.html')