from django.urls import path
from . import views


app_name = "galleryApp"
urlpatterns = [
    path('photos/', views.photos_view, name='photos_view'),
]