from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect

# Create your views here.

def dashboard(request):
    return render(request, 'Dashboard.html')

def create_ticket(request):
    return render(request, 'create_ticket.html')

def my_open_issues(request):
    return render(request, 'my_open_issues.html')
def reported_by_me(request):
    return render(request, 'reported_by_me.html')

def my_projects(request):
    return render(request, 'my_projects.html')