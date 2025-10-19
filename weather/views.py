from django.shortcuts import render
import json
import urllib.request
import os

API_KEY = os.getenv('OPENWEATHER_API_KEY')

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')

        res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
        weather_data = json.loads(res.read())
        data = {
            "country_code": str(weather_data['sys']['country']),
            "coordinate": str(weather_data['coord']['lon']) + ' ' + str(weather_data['coord']['lat']),
            "temp": str(weather_data['main']['temp']) + 'K',
            "pressure": str(weather_data['main']['pressure']),
            "humidity": str(weather_data['main']['humidity']),
            "wind": str(weather_data['wind']['speed'])
        }
    else:
        city = ''
        data = {}

    return render(request,'index.html', {'city': city, 'data': data})