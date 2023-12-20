from tkinter import *
import requests
import json
from datetime import datetime
 
#Initialize Window
 
root =Tk()
root.geometry("400x400") #size of the window by default
root.resizable(0,0) #to make the window size fixed
#title of our window
root.title("Weather")
#city_value = StringVar()
 
# ----------------------Functions to fetch and display weather info
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
def get_hourly_forcast():
    #43.71362492337767, -116.4172834600588
    return True

def get_fiveday_forecast():
    #43.71362492337767, -116.4172834600588
    return True

def getWeather():
    #Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "ae414a7e0326be0b2b0f16193e2ca3ab"  #sample API
 
    # Get city name from user from the input field (later in the code)
    city_name='Meridian' #city_value.get()
    #latitude=43.6086295
    #longitude=-116.392326

    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    #weather_url =  f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    #weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + latitude + '&lon=' + longitude +'&appid=' + api_key
    #weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=43.71&long=-116.41&appid=' + api_key
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json()  
    tfield.delete("1.0", "end")   #to clear the text field for every new output
 
    #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
  
    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
 
        #-----------Storing the fetched values of weather of a city
 
        temp_c = int(weather_info['main']['temp'] - kelvin)
        temp = (1.8 * temp_c) + 32                                     #converting default kelvin value to Celcius
        feels_like_temp_c = int(weather_info['main']['feels_like'] - kelvin)
        feels_like_temp =  (1.8 * feels_like_temp_c) + 32 
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
         
        weather = f"\
            Weather for: {city_name}\n\
            Info       : {description.capitalize()}\n\
            Temperature: {temp}°\n\
            Feels like : {feels_like_temp}°\n\
            Wind Speed : {wind_speed}\n\
            Pressure   : {pressure} hPa\n\
            Humidity   : {humidity}%\n\
            Cloud      : {cloudy}%\n\
            Sunrise    : {sunrise_time}\n\
            Sunset at  : {sunset_time}\n"
               
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name."
 
 
 
    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
 
 
 
#------------------------------Frontend part of code - Interface
 
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 16 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 18 bold').pack()
 
 
Button(root, command = getWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

#to show output
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()