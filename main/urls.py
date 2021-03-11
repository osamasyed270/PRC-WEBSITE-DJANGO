from django.contrib import admin
from django.urls import path, include

from .views import home, howToRegister, gameRules, contactUs, registerNow

urlpatterns = [
    path('', home, name='home'),
    path('how-to-register', howToRegister, name='how-to-register'),
    path('game-rules', gameRules, name='game-rules'),
    path('contact-us', contactUs, name='contact-us'),
    path('register-now', registerNow, name='register-now'),
]