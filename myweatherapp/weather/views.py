from django.shortcuts import render
import urllib.request
import json

from httpx import HTTPError

def index(request) :
    if request.method == "POST" :
        try :
            city = request.POST['city']
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=9ab82d6a05649fa6db4f34ef00a1ad46').read()
            list_of_data = json.loads(source)
            data = {
                "city_name" : str(list_of_data['name']),
                "country_code" : str(list_of_data['sys']['country']),
                "coordinates" : str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
                "temp" : str(list_of_data['main']['temp']) + chr(176)+'C',
                "pressure" : str(list_of_data['main']['pressure']),
                "humidity" : str(list_of_data['main']['humidity']),
                "main" : str(list_of_data['weather'][0]['main']),
                "description" : str(list_of_data['weather'][0]['description']),
                "icon" : str(list_of_data['weather'][0]['icon']),
            }

            print(data)
        except HTTPError as e:
            if e.response.status_code == 404:
                print("City not found")
                data = {"error_message": "City not found. Please enter a valid city name."}
            else:
                print("Error fetching weather data")
                data = {"error_message": "An error occurred while fetching weather data. Please try again later."}
    else :
        data = {}

    return render(request, 'weather/main/index.html', {'weather_data': data})