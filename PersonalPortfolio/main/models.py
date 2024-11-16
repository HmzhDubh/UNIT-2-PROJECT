from django.db import models

# Create your models here.

class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, default="None")
    message = models.TextField()
    is_viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class TechStack(models.Model):

    tool = models.CharField(max_length=50)
    preferred_color = models.CharField(max_length=50, default='E34F26')

class TechSkill(models.Model):

    skill = models.CharField(max_length=50)
    progress = models.SmallIntegerField()
