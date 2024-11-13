from django.urls import path
from . import views

app_name = "productsApp"

urlpatterns = [

    path('', views.products_view, name='products_view'),
    path('product/add/', views.add_product_view, name='add_product_view'),
    path('product/<product_id>/details/', views.product_details_view, name='product_details_view'),
    path('product/<product_id>/update/', views.update_product_view, name='update_product_view'),
    path('product/<product_id>/delete/', views.delete_product_view, name='delete_product_view'),

    path('requests/', views.requests_view, name='requests_view'),
    path('request/create/', views.create_request_view, name='create_request_view'),
    path('request/<request_id>/details/', views.request_details_view, name='request_details_view'),
    path('request/<request_id>/delete/', views.delete_request_view, name='delete_request_view'),

]