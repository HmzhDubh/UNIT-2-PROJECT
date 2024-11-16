from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('discover/hmzh/', views.about_view, name="about_view"),

    path('discover/hmzh/addTool', views.add_tool_view, name="add_tool_view"),
    path('discover/hmzh/addSkill', views.add_skill_view, name="add_skill_view"),
    path('discover/hmzh/<skill_id>/deleteSkill', views.delete_skill_view, name="delete_skill_view"),
    path('discover/hmzh/<tool_id>/deletetool', views.delete_tool_view, name="delete_tool_view"),

    path('contact/', views.contact_view, name="contact_view"),
    path('message/<message_id>/details/', views.message_details_view, name='message_details_view'),
    path('message/<message_id>/delete/', views.delete_message_view, name='delete_message_view'),
    path('testimonial/', views.testimonial_view, name='testimonial_view'),
    path('expertise/', views.expertise_view, name='expertise_view'),

]
