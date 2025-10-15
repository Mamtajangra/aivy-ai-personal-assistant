import requests         ## to  get data from internet
import os                ## to read environment variable
from dotenv import load_dotenv         ## to load env file


load_dotenv()

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")         ## here i get weather api key from env
    url =  f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  ## unit = metric because i want data in celsius
    response = requests.get(url).json()             ## get information from internet and convert to json
    temp = response["main"]["temp"]                 ## only need main portion from json
    desc = response["weather"][0]["description"]     ## need for description also
    return f"The weather in {city} is {desc} with a temperature of {temp}°C."  ## string format to find data in readable format
