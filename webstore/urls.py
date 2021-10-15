from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sdcards/', views.SDCardListView.as_view(), name='sdcards'),
    path('sdcards/<int:pk>', views.SDCardDetailView.as_view(), name='sdcard_detail'),
]
