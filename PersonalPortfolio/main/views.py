from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, SkillForm, ToolForm
from .models import Contact, TechStack, TechSkill
from galleryApp.models import Photo
from projectsApp.models import Project
from productsApp.models import Product
# Create your views here.


def home_view(request: HttpRequest):
    photos = Photo.objects.all()[0:3]

    projects = Project.objects.all()[0:3]
    products = Product.objects.all()[0:3]
    request = render(request, "index.html", context={'photos': photos, 'projects': projects, 'products': products})

    return request

def contact_view(request:HttpRequest):

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            redirect('main:home_view')
        else:
            print('Form is not valid')
            print(contact_form.errors)

    request = render(request, 'contact.html')
    return request


def about_view(request: HttpRequest):
    skills = TechSkill.objects.all()
    tools = TechStack.objects.all()

    return render(request, 'about_me.html', context={'tools': tools, 'skills':skills})

def add_tool_view(request: HttpRequest):

    if request.method == "POST":
        tool_form = ToolForm(request.POST)
        if tool_form.is_valid():
            tool_form.save()
            return redirect('/discover/hmzh/#tech-stack')
        else:
            print('Form is not valid')
            print(tool_form.errors)

    request = render(request, 'about_me.html')
    return request

def add_skill_view(request: HttpRequest):

    if request.method == "POST":
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill_form.save()
            return redirect('/discover/hmzh/#skills')
        else:
            print('Form is not valid')
            print(skill_form.errors)

    request = render(request, 'about_me.html')
    return request

def delete_skill_view(request: HttpRequest, skill_id: int):
    try:
        skill = TechSkill.objects.get(pk=skill_id)
        skill.delete()
        return redirect('dashboard:dashboard_view')
    except Exception as e:
        print(e)
        return render(request, 'page_not_found.html')

def delete_tool_view(request: HttpRequest, tool_id: int):
    try:
        tool = TechStack.objects.get(pk=tool_id)
        tool.delete()
        return redirect('dashboard:dashboard_view')
    except Exception as e:
        print(e)
        return render(request, 'page_not_found.html')
def message_details_view(request: HttpRequest, message_id: int):

    message = Contact.objects.get(pk=message_id)
    # update msg status to viewed
    message.is_viewed = True
    message.save()

    return render(request, 'message_details.html', context={'message': message})


def delete_message_view(request: HttpRequest, message_id: int):
    try:
        message = Contact.objects.get(pk=message_id)
        message.delete()
        return redirect('dashboard:dashboard_view')

    except Exception as e:
        print(e)
        return render(request, 'page_not_found.html')


def testimonial_view(request: HttpRequest):

    return render(request, 'testimonial.html')


def expertise_view(request: HttpRequest):

    return render(request, 'expertise.html')