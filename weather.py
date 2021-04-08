import tkinter as tk
import requests
import time


def getweather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=05fdaa09f4cac3887a5a831acf4fbfba"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    mintemp = int(json_data['main']['temp_min'] - 273.15)
    maxtemp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 19800))
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] - 19800))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "MAX TEMPERATURE : " + str(maxtemp) + "\n" + "MINIMAM TEPERATURE : " + str(mintemp) +"\n" + "PRESSURE : " + str(pressure) +"\n" + "HUMIDITY : " + str(humidity) + "\n" + "WIND SPEED : " +  str(wind) + "\n" + "SUNRISE : " + sunrise + "\n" + "SUNSET : " + sunset

    label1.config(text = final_info)
    label2.config(text = final_data)       
      
 
    
    
canvas = tk.Tk()
canvas.geometry("600x500")

canvas.title("WEATHER APP")

f = ("poppins", 15 , "bold")
t = ("poppins", 35 , "bold" , "italic")

textfield = tk.Entry(canvas, font = t, background = "cyan")
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getweather)

label1 = tk.Label(canvas, font = t, background = "light green")
label1.pack()
label2 = tk.Label(canvas, font = f, background = "blue")
label2.pack()

canvas.mainloop()