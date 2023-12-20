from screeninfo import get_monitors
import cv2
import os

#import numpy as np
#import time
import imutils

from tkinter import *
import requests
import json
from datetime import datetime
 
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image
    
    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        #(h, w) = image.shape[:2]
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
def get_five_day_forecast(city):
    #43.71362492337767, -116.4172834600588
    #Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "ae414a7e0326be0b2b0f16193e2ca3ab"  #sample API
 
    # Get city name from user from the input field (later in the code)
    city_name=city #'Meridian' #city_value.get()
    latitude=43.6086295
    longitude=-116.392326

    # API url
    #weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    #weather_url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly' + city_name + '&appid='+api_key
    #weather_url = 'https://api.openweathermap.org/data/2.5/forecast?' + city_name + '&appid='+api_key
    weather_url =  f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}'
    #weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + latitude + '&lon=' + longitude +'&appid=' + api_key
    #weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=43.71&long=-116.41&appid=' + api_key
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json()  
    #print(weather_info['cod'])
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
            Wind Speed : {str(round(wind_speed, 2))}\n\
            Pressure   : {pressure} hPa\n\
            Humidity   : {humidity}%\n\
            Cloud      : {cloudy}%\n\
            Sunrise    : {sunrise_time}\n\
            Sunset at  : {sunset_time}\n"
               
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name."
        
 
 
 
    #tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
    return weather
    return True

def getWeather(city):
    #Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "ae414a7e0326be0b2b0f16193e2ca3ab"  #sample API
 
    # Get city name from user from the input field (later in the code)
    city_name=city #'Meridian' #city_value.get()

    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key

    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json()  
 
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
        time_run =  (weather_info['dt'])

        #assigning Values to our weather varaible, to display as output
        weather = f"\
Weather for: {city_name}\n\
Info       : {description.capitalize()}\n\
Temperature: {temp}°\n\
Feels like : {feels_like_temp}°\n\
Wind Speed : {str(round(wind_speed, 2))}\n\
Pressure   : {pressure} hPa\n\
Humidity   : {humidity}%\n\
Cloud      : {cloudy}%\n\
Sunrise    : {sunrise_time}\n\
Sunset at  : {sunset_time}\n"
               
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name."

    return weather
 

 
#------------------------------Frontend part of code - Interface
screen = get_monitors()[3]  #set to 0 for single
print(screen)
width, height = screen.width, screen.height

#Initialize Window
root =Tk()
app=FullScreenApp(root)
root.geometry('1920x1080')#f"{width}x{height}") #size of the window by default
root.resizable(0,0) #to make the window size fixed
#title of our window
root.title("Weather")
city_value = StringVar()
format = '%m-%d %H:%M'
city_name = 'Meridian'
#city_head= Label(root, text = city_name, font = 'Arial 16 bold').pack(pady=10) #to generate label heading
#inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 18 bold').pack()
#Button(root, command = getWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

#to show output
weather = getWeather(city_name)
print(weather)

path = "images"
for file in os.listdir(path):
    if file.endswith(".png") or file.endswith(".jpg"):
        
        filename = path + '/' + os.path.join(file)
        print(filename)
        img = cv2.imread(filename)

        img_height, img_width, img_channels = img.shape
        print(f'h{img_height}, w{img_width}')
        #print(f'sh{height}, sw{width}')
        if img_width < 640 or img_height < 640:
            print('less than w')
            print('shrinking image')
            #image_resize(img, width = screen.x-2, height = screen.y-2, inter = cv2.INTER_AREA)
            #(h, w) = img.shape[:2]
            #r = img_width / float(img_height)
            #dim = (width, int(img_height * r))
    
             # resize the image
            #inter = cv2.INTER_AREA
            #resized = cv2.resize(img, dim, interpolation = inter)
            image_resize(img, width = 640, height = 640, inter = cv2.INTER_AREA)
        
        if img_width > (screen.x) and img_height > screen.y:
            #image_resize(img, width = screen.x/2, height = screen.y/2, inter = cv2.INTER_AREA)
            print('ok')
            print('shrinking image')
            #image_resize(img, width = screen.x-2, height = screen.y-2, inter = cv2.INTER_AREA)
            #(h, w) = img.shape[:2]
            r = img_width / float(img_height)
            dim = (width, int(img_height * r))
            dim = (640,640)
             # resize the image
            inter = cv2.INTER_AREA
            img = cv2.resize(img, dim, interpolation = inter)

        #img = imutils.resize(img, width=img_width, height=img_height)
        print(f"new image shape: {img.shape}")
        window_name = 'projector'
       
        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN) #WINDOW_NORMAL
        cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_AUTOSIZE,cv2.WINDOW_KEEPRATIO) # cv2.WND_PROP_FULLSCREEN
        #cv2.WINDOW_KEEPRATIO   cv2.WINDOW_FULLSCREEN

        text = weather
        coordinates = (100,100)
        font = cv2.FONT_HERSHEY_DUPLEX#SIMPLEX
        fontScale = 3
        color = (255,255,255)
        thickness = 3

        y0, dy, text = 185,80, weather
        for i, line in enumerate(text.split('\n')):
            y = y0 + i*dy
            cv2.putText(img, line, (50, y), font, fontScale, color, thickness, cv2.LINE_AA)#, False)

        #image = cv2.putText(img, text, coordinates, font, fontScale, color, thickness, cv2.LINE_AA)

        #cv2.imshow("Text", img)
        cv2.imshow("test",img) #window_name, img)

        cv2.waitKey(3000)
        #time.sleep(3)





cv2.destroyAllWindows()


