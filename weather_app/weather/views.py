from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=281ecae76cd9457c2db90d66a9289a2a'
    city = 'Delhi'
    r = requests.get(url.format(city)).json()
    city_weather = {
        'city' : r['name'],
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon']
    }

    context = {'city_weather':city_weather}
    return render(request,'weather/home.html',context)
