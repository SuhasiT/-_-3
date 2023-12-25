import datetime as dt

import requests

import json

#BASIC_URL = "http://api.openwathermap.org/data/2.5/weather?"
API_KEY = "ed23ce56ad350899dacad848dd386f1d"
user_input = input("city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={API_KEY}")

data = weather_data.json()

print("temprature",data['main']['temp'])

print("temp_max",data['main']['temp_max'])

print("temp_min",data['main']['temp_min'])

print("Humidity",data['main']['humidity'])

print("sunrise",data['sys']['sunrise'])

print("sunet",data['sys']['sunset'])




#weather = weather_data.json()['weather'][0]['main']
#temp = weather_data.json()['main']['temp']
print(weather_data.json()) 









