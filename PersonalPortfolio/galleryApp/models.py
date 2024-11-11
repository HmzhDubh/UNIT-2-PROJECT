from django.db import models

# Create your models here.

class Photo(models.Model):

    class PhotoCategory(models.TextChoices):

        Nature = "nature"
        Architecture = 'architecture'
        Portrait = 'portrait'
        Bets = 'bets'
        Aerial = 'aerial'

    title = models.CharField(max_length=20)
    about = models.TextField(max_length=120)
    url = models.ImageField(upload_to='images/', default="images/default.jpg")
    category = models.CharField(max_length=15, choices=PhotoCategory.choices)
    photo_location = models.CharField(max_length=30)
    captured_at = models.DateField()


