from django.shortcuts import render, HttpResponse, redirect
from main.models import Match_1_Register

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
    if request.method == 'POST':
        register_image = request.POST.get('register-image', 'default value')
        register_fullname = request.POST['register-fullname']
        register_email = request.POST['register-email']
        register_mobileno = request.POST['register-mobileno']
        register_gameusername = request.POST['register-gameusername']
        register_gameid = request.POST['register-gameid']
        register_age = request.POST['register-age']
        register_gender = request.POST['register-gender']
        register_facebook = request.POST['register-facebook']

        registerNow = Match_1_Register(image=register_image, full_name=register_fullname, email=register_email, mobile_no=register_mobileno, name_in_game=register_gameusername, game_id=register_gameid, age=register_age, facebook_name=register_facebook)
        registerNow.save()

        return render(request, 'main/register-now.html', {})
    else:


    # if request.method == 'POST':
    #     image = request.POST['image']
    #     full_name = request.POST['full_name']
    #     email = request.POST['email']
    #     mobile_no = request.POST['mobile_no']
    #     name_in_game = request.POST['name_in_game']
    #     game_id = request.POST['game_id']
    #     age = request.POST['age']
    #     facebook_name = request.POST['facebook_name']
    #     print(full_name, email, mobile_no, game_id)

        # registerNow = Match1(image=image, full_name=full_name, email=email, mobile_no=mobile_no, name_in_game=name_in_game, game_id=game_id, age=age, facebook_name=facebook_name)
    #     registerNow.save()
        return render(request, 'main/register-now.html', {})