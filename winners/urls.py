from django.contrib import admin
from django.urls import path, include

from .views import winners_home, match_details

urlpatterns = [
    path('', winners_home, name='winners-details'),
    path('<str:cats>/', match_details, name='match-details'),
]