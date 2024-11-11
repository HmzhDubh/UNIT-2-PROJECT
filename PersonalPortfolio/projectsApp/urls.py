from django.urls import path
from . import views

app_name = "projectsApp"

urlpatterns = [
    path('all/', views.projects_view, name='projects_view'),
    path('project/<project_id>/details', views.project_details_view, name='project_details_view'),
    path('project/add', views.add_projects_view, name='add_project_view'),
    path('project/<project_id>/update/', views.update_project_view, name='update_project_view'),
    path('project/<project_id>/delete/', views.delete_project_view, name='delete_project_view'),

]