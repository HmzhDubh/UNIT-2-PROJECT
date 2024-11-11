from django.urls import path
from . import views


app_name = "galleryApp"
urlpatterns = [
    path('photos/', views.photos_view, name='photos_view'),
    path('photos/add', views.add_photo_view, name='add_photo_view'),
    path('photos/<photo_id>/details', views.photo_details_view, name='photo_details_view'),
    path('photos/<photo_id>/delete', views.delete_photo_view, name='delete_photo_view'),
    path('photos/<photo_id>/update', views.update_photo_view, name='update_photo_view'),
]
