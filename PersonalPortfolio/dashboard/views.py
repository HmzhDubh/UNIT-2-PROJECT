from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from galleryApp.models import Photo
from projectsApp.models import Project
from main.models import Contact

# Create your views here.

def dashboard_view(request: HttpRequest):

    projects = Project.objects.all()
    messages = Contact.objects.all()
    photos = Photo.objects.all()

    if 'order_by' in request.GET:

        if request.GET['order_by'] == 'newest':

            photos = photos.order_by("-captured_at")
            messages = messages.order_by("-created_at")

        elif request.GET['order_by'] == 'oldest':

            photos = photos.order_by("captured_at")
            messages = messages.order_by("created_at")

    # filter both photos categories and project types
    if 'category' in request.GET and request.GET['data'] == 'Photos':
        photos = Photo.objects.filter(category=request.GET['category'])

    elif 'category' in request.GET and request.GET['data'] == 'Projects':
        projects = Project.objects.filter(type=request.GET['category'])

    elif 'category' in request.GET and request.GET['data'] == 'Messages':
        messages = Contact.objects.filter(is_viewed=request.GET['category'])

    # Separate each of the models in different tables
    if 'data' in request.GET:

        if request.GET['data'] == 'Projects':

            return render(request, 'dashboard.html', context={'projects': projects, 'project_cats':Project.ProjectType.choices})

        elif request.GET['data'] == 'Photos':

            return render(request, 'dashboard.html', context={'photos':photos, 'photo_cats':Photo.PhotoCategory.choices})

        elif request.GET['data'] == 'Messages':

            return render(request, 'dashboard.html', context={'messages':messages})
    # return all models
    request = render(request, 'dashboard.html', context={'messages': messages, 'projects': projects, 'photos':photos})
    request.set_cookie("active", "dashboard", max_age=60*60*24)
    return request


