from tkinter import *
import requests
import json
from datetime import datetime

#initialize window

root = Tk()
root.geometry("400x400") #size of window
root.resizable(0,0) #to make window size fixed
root.title("Weather App by Kenneth")

city_value = StringVar()

#UTC -> local time
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

#create the fetch method for the weather data

def fetchWeatherData():
    api_key = "0a138e73c9d1fff859ca0ae7fc0b6b46"
    city_name = city_value.get() # we're going to use this method later to get the name of the city from user input
    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key
    response = requests.get(weather_url) #fetch url
    weather_info = response.json()
    tfield.delete("1.0", "end") #basically a e.preventDefault()

    if weather_info['cod'] == 200:
        kelvin = 273

    
    temp = int(weather_info['main']['temp'] - kelvin) # converting to kelvin
    feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
    pressure = weather_info['main']['pressure']
    humidity = weather_info['main']['humidity']
    wind_speed = weather_info['wind']['speed'] * 3.6
    sunrise = weather_info['sys']['sunrise']
    sunset = weather_info['sys']['sunset']
    timezone = weather_info['timezone']
    cloudy = weather_info['clouds']['all']
    description = weather_info['weather'][0]['description']
 
    sunrise_time = time_format_for_location(sunrise + timezone)
    sunset_time = time_format_for_location(sunset + timezone)

#assigning Values to our weather varaible, to display as output
         
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
 
 
 
#------------------------------Frontend part of code - Interface
 
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()