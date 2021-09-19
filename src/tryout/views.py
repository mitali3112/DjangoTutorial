from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *args, **kwargs):
    print(request)
    return HttpResponse("<h1> Hello World </h1>") #string of html code

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1> Contact World </h1>") #string of html cod