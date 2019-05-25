from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    design_rating = models.IntegerField()
    usability_rating = models.IntegerField()
    content_rating = models.IntegerField()

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='media/')
    bio = models.CharField(max_length=120)
    contact_info = models.CharField(max_length=60)

    user = models.OneToOneField(User, on_delete=models.CASCADE)