from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from galleryApp.models import Photo
from projectsApp.models import Project
from main.models import Contact, TechStack, TechSkill
from productsApp.models import Product, Request


# Create your views here.

def dashboard_view(request: HttpRequest):

    projects = Project.objects.all()
    products = Product.objects.all()
    messages = Contact.objects.all()
    photos = Photo.objects.all()
    requests = Request.objects.all()
    skills = TechSkill.objects.all()
    tools = TechStack.objects.all()

    # order models as newest or oldest
    if 'order_by' in request.GET:

        if request.GET['order_by'] == 'newest':

            photos = photos.order_by("-captured_at")
            messages = messages.order_by("-created_at")
            products = products.order_by("-created_at")
            requests = requests.order_by("-ordered_at")

        elif request.GET['order_by'] == 'oldest':

            photos = photos.order_by("captured_at")
            messages = messages.order_by("created_at")
            products = products.order_by("created_at")
            requests = requests.order_by("ordered_at")

    # filter both photos categories and project types
    if 'category' in request.GET and request.GET['data'] == 'Photos':
        if request.GET['category'] != 'all':
            photos = Photo.objects.filter(category=request.GET['category'])

    elif 'category' in request.GET and request.GET['data'] == 'Projects':
        if request.GET['category'] != 'all':
            projects = Project.objects.filter(type=request.GET['category'])

    elif 'category' in request.GET and request.GET['data'] == 'Products':
        if request.GET['category'] != 'all':
            products = Product.objects.filter(type=request.GET['category'])

    elif 'category' in request.GET and request.GET['data'] == 'Messages':

        if request.GET['category'] == 'viewed':

            messages = Contact.objects.filter(is_viewed=True)
        elif request.GET['category'] == 'not_viewed':
            messages = Contact.objects.filter(is_viewed=False)

    elif 'category' in request.GET and request.GET['data'] == 'Requests':
        if request.GET['category'] != 'all':
            requests = Request.objects.filter(type=request.GET['category'])

    # Separate each of the models in different tables
    if 'data' in request.GET:

        if request.GET['data'] == 'Projects':

            return render(request, 'dashboard.html', context={'projects': projects, 'project_cats':Project.ProjectType.choices})
        elif request.GET['data'] == 'Products':

            return render(request, 'dashboard.html', context={'products': products, 'product_cats':Product.ProductType.choices})

        elif request.GET['data'] == 'Requests':

            return render(request, 'dashboard.html', context={'requests': requests, 'request_cats':Request.RequestType.choices})

        elif request.GET['data'] == 'Photos':

            return render(request, 'dashboard.html', context={'photos':photos, 'photo_cats':Photo.PhotoCategory.choices})

        elif request.GET['data'] == 'Messages':

            return render(request, 'dashboard.html', context={'messages':messages})

        elif request.GET['data'] == 'Skills':

            return render(request, 'dashboard.html', context={'skills':skills})
        elif request.GET['data'] == 'Tools':

            return render(request, 'dashboard.html', context={'tools':tools})

    # return all models
    request = render(request, 'dashboard.html', context={'tools':tools, 'skills':skills, 'messages': messages, 'projects': projects, 'products': products, 'photos': photos, 'requests': requests})

    return request


