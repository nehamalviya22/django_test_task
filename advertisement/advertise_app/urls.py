from django.contrib import admin
from django.urls import path
from .views import GetAd,Impression,GetStats

urlpatterns = [
    path('GetAd/', GetAd.as_view()),
    path('Impression/', Impression.as_view()),
    path('GetStats/', Getstats.as_view()),
]