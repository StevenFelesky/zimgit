from django.contrib import admin

from .models import Hotspot, SDCard, Download

admin.site.register(SDCard)
admin.site.register(Download)
admin.site.register(Hotspot)
