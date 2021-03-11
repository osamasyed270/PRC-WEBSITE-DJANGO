from django.shortcuts import render, HttpResponse, redirect
from main.models import Match_1_Register
from django.core.files.storage import FileSystemStorage

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
    if request.method == 'POST' and request.FILES['register-image']:
        myfile = request.FILES['register-image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        new_register = Match_1_Register(
            image = url,
            full_name = request.POST['register-fullname'],
            email = request.POST['register-email'],
            mobile_no = request.POST['register-mobileno'],
            name_in_game = request.POST['register-gameusername'],
            game_id = request.POST['register-gameid'],
            age = request.POST['register-age'],
            facebook_name = request.POST['register-facebook']
        )
        new_register.save()
        return render(request, 'main/register-now.html')
    else:
        pass    
    
    return render(request, 'main/register-now.html')