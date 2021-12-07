from django.contrib import admin
from django.urls import path
from .views import GetAd,Impression

urlpatterns = [
    path('GetAd/', GetAd.as_view()),
    path('Impression/', Impression.as_view()),
]