from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .models import Profile
from .forms import RegistrationForm, edit_profile, LoginForm, ProfileForm
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
import requests
import os

# Create your views here.

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a86ec00546efa9910a536f062c0bfbab'
        city = request.user.Profile.city
        r = requests.get(url.format(city)).json()

        if r.get('message') == 'city not found':
            content = {'user': request.user,
                 'profile': request.user.Profile,
                   'city': city,
                   'temperature': 'No Data',
                   'description': 'invalid city',
                   'icon': 'invalid city',}
            return render(request, "Accounts/account_view.html", content)

        else:
            content = {'user': request.user,
                 'profile': request.user.Profile,
                   'city': request.user.Profile.city,
                   'temperature': r['main']['temp'],
                   'description': r['weather'][0]['description'],
                   'icon': r['weather'][0]['icon'],
                   }

            return render(request, "Accounts/account_view.html",content)

def account_create_view(request):
    email=''
    subject='Welcome!'
    message='Welcome to my Website! Since this website is written in python django please let me know features you would like to see on the website! \n -Idan Lau'

    registration = RegistrationForm(request.POST or None)
    profile = ProfileForm(request.POST or None,request.FILES or None)
    content = {"registration": registration, "profile":profile}

    if registration.is_valid() and profile.is_valid():
        email = registration.cleaned_data.get("email")
        user = registration.save()

        Profile.objects.create(
            user= user,
            description = profile.cleaned_data['description'],
            image = profile.cleaned_data['image'],
            city = profile.cleaned_data['city'],

        )
        print('sent')
        send_mail(subject, message, 'lauidan31@gmail.com', [email])

        return redirect('/account/profile/')


    return render (request, "registration/register.html",content)


class CustomLoginView(LoginView):
    template_name = "login/login.html"  # your template
    from_class = LoginForm
    redirect_authenticated_user = True

def logout_view(request):
    logout(request)
    return redirect('/')

def edit_profile_view(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    current = request.user.Profile
    data = {'description' : current.description}
    form = edit_profile(request.POST or None,request.FILES or None,instance=current, initial=data)
    del_img = current.image
    del_path = current.image.path

    if request.method == "POST":

        if form.is_valid():
            img_input = form.cleaned_data['image']
            if del_img != img_input:
                os.remove(del_path )
            form.save()


            return redirect('/account/profile/')
        else:
            form = edit_profile(instance = current)



    return render(request, "Accounts/edit_profile.html", {"form":form,  'profile': request.user.Profile})




