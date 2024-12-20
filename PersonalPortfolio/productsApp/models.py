from django.db import models

# Create your models here.

class Product(models.Model):

    class ProductType(models.TextChoices):

        preset_filter = 'Preset Filter'
        photo_session = 'Photo Session'
        programming_project = 'Programming Project'
        consultant = 'Consultant'

    title = models.CharField(max_length=120)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=ProductType.choices)
    image = models.ImageField(upload_to='images/', default="images/default.jpg")
    quantity = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class Request(models.Model):

    class RequestType(models.TextChoices):

        preset_filter = 'Preset Filter'
        photo_session = 'Photo Session'
        programming_project = 'Programming Project'
        consultant = 'Consultant'

    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=RequestType.choices)
    quantity = models.SmallIntegerField(default=1)
    ordered_at = models.DateTimeField(auto_now_add=True)
    # Client information
    client_name = models.CharField(max_length=100, default='none')
    client_email = models.CharField(max_length=100, default='none')
    client_note = models.TextField(default='none')
