from django.contrib import admin
from django.urls import path
from .views import GetAd

urlpatterns = [
    path('GetAd/', GetAd.as_view()),
]