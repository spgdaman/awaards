from django.db import models

class Project(models.Model):
    image = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=200)
    design_rating = models.IntegerField()
    usablity_rating = models.IntegerField()
    content_rating = models.IntegerField()

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='media/')
    bio = models.CharField(max_length=120)
    contact_info = models.CharField(max_length=60)