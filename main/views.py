from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from main.models import Match_1_Register
from django.core.files.storage import FileSystemStorage
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def howToRegister(request):
    return render(request, 'main/how-to-register.html')

def gameRules(request):
    return render(request, 'main/game-rules.html')

def contactUs(request):
    return render(request, 'main/contact-us.html')

def allRegistersDetails(request):
    all_registers = Match_1_Register.objects.all()
    return render(request, 'main/all-registers-details.html', {'registers': all_registers})

def registerNow(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, '<b>Thank You!</b> Your submission has been sent.')
            return HttpResponseRedirect('/register-now')

        else:
            messages.error(request, '<b>Error!</b> Please fill all the fields.')
        
    
    context = {'form': form}
    return render(request, 'main/register-now.html', context)

    # if request.method == 'POST' and request.FILES['register-image']:
    #     myfile = request.FILES['register-image']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     url = fs.url(filename)
    #     new_register = Match_1_Register(
    #         image = url,
    #         full_name = request.POST['register-fullname'],
    #         email = request.POST['register-email'],
    #         mobile_no = request.POST['register-mobileno'],
    #         name_in_game = request.POST['register-gameusername'],
    #         game_id = request.POST['register-gameid'],
    #         age = request.POST['register-age'],
    #         gender = request.POST['register-gender'],
    #         facebook_name = request.POST['register-facebook']
    #     )
    #     new_register.save()
    #     return HttpResponseRedirect(request.path)
    #     # return render(request, 'main/register-now.html')
    # else:
    #     pass    
    
        # return render(request, 'main/register-now.html')