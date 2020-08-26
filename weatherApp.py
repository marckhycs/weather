from tkinter import Tk
from tkinter import Label
from bs4 import BeautifulSoup
import requests
from PIL import ImageTk, Image




url = "https://weather.com/weather/today/l/13.91,121.05?par=google&temp=c"

def gatherInfo():
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")

    locationItem = soup.find('h1', class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--location--1YWj_').text
    timeItem = soup.find('div', class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--timestamp--1ybTk').text
    temperatureItem = soup.find('span', class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY').text
    indicatorItem = soup.find('div', class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--phraseValue--mZC_p').text
    chanceItem = soup.find('div', class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf').text

    test = indicatorItem.lower()
    if test == "mostly cloudy" or test == "partly cloudy":
        picture.config(image = cloudy)
    elif test == "sunny" or test == "mostly sunny" or  test == "fair":
        picture.config(image = sunny)
    else:
        picture.config(image = rainy)

    
    location.config(text = locationItem)
    time.config(text = timeItem)
    temperature.config(text = temperatureItem)
    indicator.config(text = indicatorItem)
    chance.config(text = chanceItem)
   
    temperature.after(20000, gatherInfo)
    screen.update()


   


def mainScreen():
    global screen
    global location
    global time
    global temperature
    global indicator
    global chance
    global sunny
    global rainy
    global cloudy
    global picture

    screen = Tk()
    screen.config(bg = 'white')
    screen.iconbitmap('C:/Users/MARCKYCS/Desktop/weather/images/weather.ico')
    screen.title("Weather Forecast")
    
    #Images
    sunny = Image.open('images/sunny.jpg')
    sunny = sunny.resize((50, 50), Image.ANTIALIAS)
    sunny = ImageTk.PhotoImage(sunny)

    rainy = Image.open('images/rainy.jpg')
    rainy = rainy.resize((50, 50), Image.ANTIALIAS)
    rainy = ImageTk.PhotoImage(rainy)

    cloudy = Image.open('images/cloudy.jpg')
    cloudy = cloudy.resize((50, 50), Image.ANTIALIAS)
    cloudy = ImageTk.PhotoImage(cloudy)

    location = Label(screen, font = ("Calibri", 12), bg = 'white')
    location.grid(row = 0, sticky = "N", pady = 5, padx = 5)

    time = Label(screen, font =('Calibri', 8), bg = 'white')
    time.grid(row = 1, sticky = "W", padx = 5)

    picture = Label(screen, bg = 'white')
    picture.grid(row = 2, sticky = "E", padx= 25)

    temperature = Label(screen, font = ("Helvetica",40), bg = 'white')
    temperature.grid(row = 2, sticky = "N", padx = 5)

    indicator = Label(screen, font = ("Helvetica", 12), bg = 'white')
    indicator.grid(row = 3, sticky = "W")

    chance = Label(screen, font = ("Helvetica", 8), bg = 'white')
    chance.grid(row = 4, sticky = "W")
    
    gatherInfo()

    
    screen.mainloop()
mainScreen()
