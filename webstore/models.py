from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class SDCard(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of this item.')

    def __str__(self):
        return self.name

class Download(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of this item.')

    def __str__(self):
        return self.name
    
class Hotspot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of this item.')

    def __str__(self):
        return self.name