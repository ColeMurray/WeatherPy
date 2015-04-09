#!venv/bin/python

from urllib2 import Request, urlopen, URLError
import json
from collections import defaultdict
from APIKEY import APIKEY
def getWeather(cityname):
    weather = urlopen('http://api.wunderground.com/api/' + APIKEY + '/hourly/q/CA/' + cityname + '.json')
    json_response = weather.read()
    parsedResponse = json.loads(json_response)
    filename = cityname + '.json'
    with open(filename,"wb") as outfile:
        json.dump(parsedResponse,outfile,indent=6)

def getWeatherFromFile(filename):
    location = open(filename)
    data = json.load(location)
    weather_data = defaultdict(list)
    #list of dicts in file
    weatherdata = data["hourly_forecast"]
    
    #Get the current hour
    item = weatherdata[0];
    prettyString = item['FCTTIME']['pretty']
    condition = item['condition']

    weather_data[0].append(prettyString)
    weather_data[0].append(condition)
    return weather_data

def getWeather_pub(cityname):
    getWeather(cityname)
    weather_data = getWeatherFromFile(cityname + '.json')
    return weather_data

