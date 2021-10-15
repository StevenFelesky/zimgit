from django.contrib import admin

from .models import Hotspot, SDCard, ZimFile

admin.site.register(SDCard)
admin.site.register(ZimFile)
admin.site.register(Hotspot)
