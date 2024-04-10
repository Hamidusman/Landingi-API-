from django.db import models
from datetime import date
# Create your models here.

class Experience(models.Model):
    Position = models.CharField(max_length = 50)
    Organisation = models.CharField(max_length = 100)
    Description = models.CharField(max_length = 1000)
    Started = models.DateField(max_length = 20)
    Ended = models.DateField(default = 'Present', max_length = 20)
