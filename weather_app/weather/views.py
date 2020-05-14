from django.shortcuts import render, redirect
from django.forms import ValidationError
import requests
from .models import City
from .forms import CityForm,feedback_form,contact_form,UserRegisterForm,UserLoginForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
# Create your views here.

def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=281ecae76cd9457c2db90d66a9289a2a'
    cities = City.objects.all()
    weather_data = []
    message1 = ''
    message2 = ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        form1 = feedback_form(request.POST)
        if form1.is_valid():
            return render(request,'weather/thanks.html')
        else:
            try:
                form.save()
            except:
                message1 = "Already in the list!"
                message2 = "Please enter another location."

    form = CityForm()
    form1 = feedback_form()

    for city in cities:
        r = requests.get(url.format(city)).json()
        # Handling KeyError
        try:
            city_weather = {
                'city' : r['name'],
                'temperature' : r['main']['temp'],
                'humidity' : r['main']['humidity'],
                'wind':r['wind']['speed'],
                'pressure' : r['main']['pressure'],
                'clouds':r['clouds']['all'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon']
            }
            weather_data.append(city_weather)
        except:
            obj = City.objects.latest('name')
            obj.delete()
            message1 = "No such location found!"
            message2 = "Please enter again"
            continue

    context = {
        'weather_data':weather_data,
        'form':form,'form1':form1,
        'message1':message1,
        'message2':message2,
    }
    return render(request,'weather/home.html',context)

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    message=''
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request,user)
        if next:
            return redirect(next)
        message = "Welcome "+username+"!"
        return render(request,"weather/home.html",{'message':message})
    context = {
        'form':form,
    }
    return render(request,"weather/login.html",context)

def signup_view(request):
    if  request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    context = {
        'form' : form,
    }

    return render(request,'weather/signup.html',context)

def logout_view(request):
    logout(request)
    context={'message':'You have been logged out successfully.'}
    return render(request,'weather/home.html',context)

def account_view(request):
    return render(request,'weather/account.html'    )

def reset(request):
    for obj in City.objects.all():
        obj.delete()

    return redirect('../')

def about(request):
    return render(request,'weather/about.html')

def contact(request):

    if request.method == 'POST':
        form = contact_form(request.POST)
        form.save()
        return render(request,'weather/thanks.html')

    form = contact_form()
    context = {'form':form}
    return render(request,'weather/contact.html',context)
