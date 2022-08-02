
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests


import json
from .forms import *


# Create your views here.
def zillow(request):
    address = request.POST["address"]
    city = request.POST["city"]
    state = request.POST["state"] 
    zip = request.POST["zip"]
    print(request.POST)
    stored_data = []
     
    url = "https://zillow56.p.rapidapi.com/search"

    querystring = {"location":f'{address}. {city},{state}. {zip}'}

    headers = {
	"X-RapidAPI-Key": "42123ed4f1msh64988eb134ebadcp1a8ce1jsn4fa401f0b51a",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}
    
  

    response = requests.request("GET", url, headers=headers, params=querystring)
    stored_data.append(response)
    parse_json = json.loads(response.text)
    display_data = parse_json.keys()
    # print(display_data)
    # print(parse_json)
    
    longitude = parse_json['longitude']
    latitude  = parse_json['latitude']
    weather_url = "https://visual-crossing-weather.p.rapidapi.com/history"

    weather_querystring = {"startDateTime":"2019-01-01T00:00:00","aggregateHours":"24","location":f'{address}. {city},{state}. {zip}',"endDateTime":"2019-01-03T00:00:00","unitGroup":"us","dayStartTime":"8:00:00","contentType":"json","dayEndTime":"17:00:00","shortColumnNames":"0"}

    weather_headers = {
	"X-RapidAPI-Key": "a734b12ec8msh6f0fe8ed4e1ba42p170be5jsn34eb295dbddb",
	"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
}

    weather_response = requests.request("GET", weather_url, headers=weather_headers, params=weather_querystring)
    weather_json = json.loads(weather_response.text)
    weather_data = weather_response.json()
    dew = weather_json['columns']['dew']['id']
    temp = weather_json['columns']['values']['temp']
    temp_max = weather_json['columns']['values']['maxt']
    temp_min = weather_json['columns']['values']['mint']
    precip = weather_json['columns']['values']['precip']
    dew = weather_json['columns']['values']['dew']
    humidity = weather_json['columns']['values']['humidity']
    solarenergy = weather_json['columns']['values']['solarenergy']
    cloudcover = weather_json['columns']['values']['cloudcover']
    print(weather_json['columns'].keys())
    print("FREAKING PRINT")

    context = {'weather_response':weather_json, 'dew': dew }

    return render (request,'users.html', context)

   



def new(request):
    form = InputForm()
    return render(request, 'new.html', {"form":form })