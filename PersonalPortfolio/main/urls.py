from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('discover/hmzh/', views.about_view, name="about_view"),
    path('contact/', views.contact_view, name="contact_view"),
    path('message/<message_id>/details/', views.message_details_view, name='message_details_view'),
    path('message/<message_id>/delete/', views.delete_message_view, name='delete_message_view'),
    path('testimonial/', views.testimonial_view, name='testimonial_view'),
    path('expertise/', views.expertise_view, name='expertise_view'),

]
