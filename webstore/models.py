from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter genre (e.g. Survival): ')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class SDCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of files included.')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this SD card')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


