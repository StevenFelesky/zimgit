from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class SDCard(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of this item.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sdcard_detail', args=[str(self.id)])

class ZimFile(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of this item.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('zimfile-info', args=[str(self.id)])
    
class Hotspot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of this item.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hotspot-info', args=[str(self.id)])