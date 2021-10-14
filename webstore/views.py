from django.shortcuts import render

from .models import SDCard, Genre

def index(request):

    # Generate counts of some of the main objects
    num_cards = SDCard.objects.all().count()
    num_genres = Genre.objects.all().count()

    context = {
        'num_cards': num_cards,
        'num_genres': num_genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
