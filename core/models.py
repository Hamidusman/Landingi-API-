from django.db import models
from django.contrib.auth.models import User
from datetime import date
from autoslug import AutoSlugField
from django_countries.fields import CountryField
# Create your models here.

class Profile(models.Model):
    firstame = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    phone = models.IntegerField(default = '+2348170371922')
    country = CountryField(default='NG')
    city = models.CharField(max_length= 20)
    address = models.CharField(max_length= 100)
    Dob = models.DateField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from ='firstname')

class Education(models.Model):
    Institution = models.CharField(max_length = 100)
    Certificate= models.CharField(max_length = 60)
    Started = models.DateField(max_length = 20)
    Ended = models.DateField(default = 'Present', max_length = 20)
    Location = models.CharField(max_length = 50)


class Experience(models.Model):
    position = models.CharField(max_length = 50)
    organisation = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    started = models.DateField(max_length = 20)
    ended = models.DateField(default = 'Present', max_length = 20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from ='position')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.certificate

class Link(models.Model):
    website = models.CharField(max_length = 50, default= '')
    x = models.CharField(max_length = 50, default = '')
    facebook = models.CharField(max_length = 50, default= '')
    linkedIn = models.CharField(max_length = 50, default= '')
    github = models.CharField(max_length = 50, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.github