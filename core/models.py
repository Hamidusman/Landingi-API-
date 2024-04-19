from django.db import models
from django.contrib.auth.models import User
from datetime import date
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=8)


class Profile(models.Model):
    firstname = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    phone = models.IntegerField(default = '+2348170371922')
    country = CountryField(default='NG')
    city = models.CharField(max_length= 20)
    address = models.CharField(max_length= 100)
    Dob = models.DateField(null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from ='firstname')

class Education(models.Model):
    Institution = models.CharField(max_length = 100)
    Certificate= models.CharField(max_length = 60)
    Started = models.DateField(max_length = 20)
    Ended = models.DateField(default = 'Present', max_length = 20)
    Location = models.CharField(max_length = 50)
    slug = AutoSlugField(populate_from ='certificate')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Experience(models.Model):
    position = models.CharField(max_length = 50)
    organisation = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    started = models.DateField(max_length = 20)
    ended = models.DateField(default = 'Present', max_length = 20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from ="position", unique=True)

    def __str__(self):
        return self.certificate

class Link(models.Model):
    website = models.CharField(max_length = 50, default= '')
    x = models.CharField(max_length = 50, default = '')
    facebook = models.CharField(max_length = 50, default= '')
    linkedIn = models.CharField(max_length = 50, default= '')
    github = models.CharField(max_length = 50, )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from ='github')

    def __str__(self):
        return self.github