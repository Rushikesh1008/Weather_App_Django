from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=281ecae76cd9457c2db90d66a9289a2a'
    cities = City.objects.all()
    weather_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : r['name'],
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    context = {'weather_data':weather_data,'form':form}
    return render(request,'weather/home.html',context)
