from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('sdcards/', views.SDCardListView.as_view(), name='sdcards'),
    path('hotspots/', views.HotspotListView.as_view(), name='hotspots'),
    path('downloads/', views.DownloadListView.as_view(), name='downloads'),
    path('contact-us/', views.contact_us, name='contact-us'),
]

urlpatterns += staticfiles_urlpatterns()