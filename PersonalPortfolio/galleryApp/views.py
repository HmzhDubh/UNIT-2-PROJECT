from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm
# Create your views here.


def photos_view(request: HttpRequest):
    photos = Photo.objects.all()
    # if request.method == "GET" and request.GET['category'] == :

    request = render(request, 'photos.html', context={'photos': photos})
    request.set_cookie("active", "gallery", max_age=60*60*24)
    return request


def add_photo_view(request: HttpRequest):
    if request.method == 'POST':
        print(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            photo_form.save()
            return redirect('dashboard:dashboard_view')
        else:
            print("Form is not Valid")

    request = render(request, 'add_photo.html', context={'photo_cats': Photo.PhotoCategory.choices})
    request.set_cookie("active", "gallery", max_age=60*60*24)
    return request


def photo_details_view(request: HttpRequest, photo_id: int):

    photo = Photo.objects.get(pk=photo_id)

    request = render(request, 'photo_details.html', context={'photo': photo})
    request.set_cookie("active", "gallery", max_age=60*60*24)
    return request


def update_photo_view(request: HttpRequest, photo_id: int):
    photo = Photo.objects.get(pk=photo_id)
    if request.method == "POST":
        photo_form = PhotoForm(request.POST, request.FILES, instance=photo)
        if photo_form.is_valid():
            photo_form.save()
            request = redirect('galleryApp:photo_details_view', photo_id=photo.id)
            request.set_cookie("active", "gallery", max_age=60*60*24)
            return request
    request = render(request, 'update_photo.html', context={'photo_cats': Photo.PhotoCategory.choices,'photo': photo})
    request.set_cookie("active", "gallery", max_age=60*60*24)
    return request


def delete_photo_view(request: HttpRequest, photo_id: int):

    try:
        photo = Photo.objects.get(pk=photo_id)
        photo.delete()
        return redirect('dashboard:dashboard_view')

    except Exception as e:
        print(e)
        return render(request, 'page_not_found.html')
