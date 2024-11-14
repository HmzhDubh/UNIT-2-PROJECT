from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.

def projects_view(request: HttpRequest):

    projects = Project.objects.all()
    print(projects)
    request = render(request, 'projects.html', context={'projects': projects})
    return request

def project_details_view(request: HttpRequest, project_id):

    project = Project.objects.get(pk=project_id)

    request = render(request, 'project_details.html', context={'project': project})
    return request


def add_projects_view(request: HttpRequest):

    if request.method == 'POST':
        print(request.POST)
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project_form.save()
            return redirect('projectsApp:projects_view')
        else:
            print("Form is not Valid")

    request = render(request, 'add_project.html', context={'project_cats':Project.ProjectType.choices})
    return request


def update_project_view(request: HttpRequest, project_id: int):

    project = Project.objects.get(pk=project_id)

    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES, instance=project)

        if project_form.is_valid():
            project_form.save()
            request = redirect('dashboard:dashboard_view')
            return request

    request = render(request, 'update_project.html', context={'project': project, 'project_cats': Project.ProjectType.choices})
    return request

def delete_project_view(request: HttpRequest, project_id: int):
    try:

        project = Project.objects.get(pk=project_id)
        project.delete()
        return redirect('dashboard:dashboard_view')

    except Exception as e:
        return render(request, 'page_not_found.html')
