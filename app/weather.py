import requests
import json
from app import app

def getWeather(zipcode):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip={},us&APPID=05d9b0402f0ee1732ef71262e6467299'.format(zipcode))
    if r.status_code != 200:
        return 'Error: weather service failed.'
    s = json.loads(r.content.decode('utf-8-sig'))
    weather = s["weather"][0]['main']
    temp = s["main"]["temp"]
    return "weather:{}    temp:{}K".format(weather, str(temp))