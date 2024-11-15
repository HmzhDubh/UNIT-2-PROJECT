from django import forms
from .models import Product, Request
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "type",
            "image",
            "quantity",
        ]

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            "title",
            "description",
            "type",
            "quantity",
            "client_name",
            "client_email",
            "client_note",
        ]
