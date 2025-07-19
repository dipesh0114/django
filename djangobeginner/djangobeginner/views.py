from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world! This is the home page of the Django beginner project.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is the about page of the Django beginner project.")

def contact(request):
    return HttpResponse("This is the contact page of the Django beginner project.")

