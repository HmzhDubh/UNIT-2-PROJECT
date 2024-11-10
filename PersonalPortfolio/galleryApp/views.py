from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def photos_view(request: HttpRequest):

    request = render(request, 'photos.html')
    return request