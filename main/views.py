from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def howToRegister(request):
    return render(request, 'main/how-to-register.html')

def gameRules(request):
    return render(request, 'main/game-rules.html')

def contactUs(request):
    return render(request, 'main/contact-us.html')

def registerNow(request):
    return render(request, 'main/register-now.html')