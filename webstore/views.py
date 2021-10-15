from django.shortcuts import render
from django.views import generic

from .models import Hotspot, SDCard, ZimFile

def index(request):

    # Generate counts of some of the main objects
    num_cards = SDCard.objects.all().count()
    num_files = ZimFile.objects.all().count()
    num_hotspot = Hotspot.objects.all().count()

    name = SDCard

    context = {
        'num_cards': num_cards,
        'num_genres': num_files,
        'num_hotspot': num_hotspot,
        'name': name,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class SDCardListView(generic.ListView):
    model = SDCard
    context_object_name = 'sdcards'
    queryset = SDCard.objects.filter()
    template_name = 'sdcards.html'
    
class SDCardDetailView(generic.DetailView):
    model = SDCard

