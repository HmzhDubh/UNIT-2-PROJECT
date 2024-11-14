from django.db import models

# Create your models here.

class Project(models.Model):

    class ProjectType(models.TextChoices):
        Web_Application = "Web Application"
        Mobile_Application = 'Mobile Application'
        IAAS = 'Infrastructure As A Service'
        Cloud = 'Cloud'
        ServerLess = 'Server Less Application'

    title = models.CharField(max_length=50)
    about = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    type = models.CharField(max_length=120, choices=ProjectType.choices)
    status = models.BooleanField(default=True)
    link = models.CharField(max_length=1024)