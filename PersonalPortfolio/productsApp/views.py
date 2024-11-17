from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm, RequestForm
from .models import Product, Request
# Create your views here.

# Products
def products_view(request:HttpRequest):

    projects = Product.objects.all()

    request = render(request, 'products.html', context={'products': projects})

    return request


def add_product_view(request: HttpRequest):

    if request.method == 'POST':

        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            product_form.save()
            return redirect('dashboard:dashboard_view')
        else:
            print("Form is not Valid")

    return render(request, 'add_product.html', context={'product_types':Product.ProductType.choices})


def update_product_view(request: HttpRequest, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':

        product_form = ProductForm(request.POST, request.FILES, instance=product)

        if product_form.is_valid():
            product_form.save()
            return redirect('dashboard:dashboard_view')
        else:
            print("Form is not Valid")


    return render(request, 'update_product.html', context={'product': product, 'product_types': Product.ProductType.choices})


def product_details_view(request: HttpRequest, product_id: int):

    product = Product.objects.get(pk=product_id)

    return render(request, 'product_details.html', context={'product': product})


def delete_product_view(request: HttpRequest, product_id: int):

    try:
        product = Product.objects.get(pk=product_id)
        product.delete()

    except Exception as e:
        render(request, 'page_not_found.html')

    return redirect('dashboard:dashboard_view')


# Requests
def requests_view(request:HttpRequest):

    requests = Request.objects.all()

    request = render(request, 'requests.html', context={'requests': requests})

    return request


def create_request_view(request: HttpRequest, product_id):

    product = Product.objects.get(pk=product_id)

    if request.method == "POST":
        request_form = RequestForm(request.POST)
        if request_form.is_valid():
            request_form.save()
            product_quantity = int(product.quantity)
            product_quantity -= int(request.POST['quantity'])
            product.quantity = product_quantity
            product.save()
            print("update quantity of product", product.quantity)
            return render(request, 'page_success.html')
        else:
            print('Form is not valid')
            print(request_form.errors)

    request = render(request, 'new_request.html', context={'product': product,'request_types': Request.RequestType.choices})
    return request


def request_details_view(request: HttpRequest, request_id: int):

    the_request = Request.objects.get(pk=request_id)

    return render(request, 'request_details.html', context={'the_request': the_request})


def delete_request_view(request: HttpRequest, request_id: int):

    try:
        the_request = Request.objects.get(pk=request_id)
        the_request.delete()

    except Exception as e:
        render(request, 'page_not_found.html')

    return redirect('dashboard:dashboard_view')