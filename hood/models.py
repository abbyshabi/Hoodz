from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.conf import settings

class Neighbourhood(models.Model):
   """
   This is the class we will use to create images
   """
   n_image_url = models.ImageField(upload_to = "images/")
   neigh_name = models.CharField(max_length = 30)
   neigh_description = models.TextField(max_length=100)
   neigh_admin = models.ForeignKey(User,related_name='neigh',on_delete=models.CASCADE)
   neigh_date = models.DateTimeField(auto_now_add = True,null = True)
   location = models.CharField(max_length = 30)
   occupants = models.IntegerField(default = 0)


class Project(models.Model):
   """
   This is the class we will use to create images
   """
   image_url = models.ImageField(upload_to = "images/")
   name = models.CharField(max_length = 30)
   description = models.TextField(max_length=100)
   admin = models.ForeignKey(User,related_name='images',on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now_add = True,null = True)
   location = models.CharField(max_length = 30)
   occupants = models.IntegerField(default = 0)
   

    
   def save_project(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

   def delete_project(self):
       """
       This is the function that we will use to delete the instance of this class
       """
       self.delete()
    
   def get_absolute_url(self): 
        return reverse('home') 


   def __str__(self):
        return self.name

class Profile(models.Model):
    profile_image = models.ImageField(blank=True,upload_to='profiles/')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    neighbour_hood = models.ForeignKey(Project,on_delete = models.CASCADE)

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    def get_absolute_url(self): 
        return reverse('user_profile')

class Business(models.Model):
    about = models.TextField(max_length=100)
    name = models.TextField(max_length=15)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business')
    neighbourhood = models.ForeignKey(Project,on_delete = models.CASCADE)

    def save_profile(self):
        self.save()

      
    @classmethod
    def get_by_id(cls, id):
        business = Business.objects.get(id = id)
        return profile

    
    def get_absolute_url(self): 
        return reverse('business')

    def __str__(self):
        return self.name

    @classmethod
    def get_business(cls, id):
        business = Business.objects.filter(neighbourhood__pk =id)
        return business
