from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields =[
            "title",
            "about",
            "url",
            "category",
            "photo_location",
            "captured_at",
        ]
