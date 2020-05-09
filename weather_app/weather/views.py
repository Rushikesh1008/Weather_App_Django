from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm,feedback_form
# Create your views here.

def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=281ecae76cd9457c2db90d66a9289a2a'
    cities = City.objects.all()
    weather_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        form1 = feedback_form(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'weather/thanks.html')
        else:
            form.save()

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
            continue

    context = {'weather_data':weather_data,'form':form,'form1':form1}
    return render(request,'weather/home.html',context)

def reset(request):
    for obj in City.objects.all():
        obj.delete()

    return redirect('../')

def about(request):
    return render(request,'weather/about.html')

def contact(request):
    return render(request,'weather/contact.html')
