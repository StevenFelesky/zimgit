from django.shortcuts import render
from django.views import generic

from .models import Download, Hotspot, SDCard

def index(request):
    return render(request, 'index.html')

def details(request):
    return render(request, 'details.html')

def contact_us(request):
    return render(request, 'contact-us.html')

class SDCardListView(generic.ListView):
    model = SDCard
    context_object_name = 'sdcards'
    queryset = SDCard.objects.filter()
    template_name = 'sdcards.html'

class HotspotListView(generic.ListView):
    model = Hotspot
    context_object_name = 'hotspots'
    queryset = Hotspot.objects.filter()
    template_name = 'hotspots.html'

class DownloadListView(generic.ListView):
    model = Download
    context_object_name = 'downloads'
    queryset = Download.objects.filter()
    template_name = 'downloads.html'
