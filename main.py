from tkinter import*
import webbrowser
import os
import datetime
import random
import requests
from tkinter.messagebox import showinfo
from translate import translate
import time
api_key="ecffd157b2cc9eacbd0d35a45c3dc047"
base_url="https://api.openweathermap.org/data/2.5/weather?"

screen = Tk()
def Meteo():
    fileVille=open("Config/Ville.txt","r")
    varVille=str(fileVille.readlines()[0])
    complete_url=base_url+"appid="+api_key+"&q="+varVille+"&lang=fr"+"&units=metric"
    reponse=requests.get(complete_url).json()
    if reponse["cod"]!="404":
        DICT=reponse["main"]
        temp=DICT["temp"]
        humidity=DICT["humidity"]
        meteodet=reponse["weather"][0]["description"]
        print(temp,"\n",humidity,"\n",meteodet)
screen.title("Ryley")
screen.maxsize(500,700)
screen.minsize(500,700)
screen.iconphoto(False,PhotoImage(file="image/Ryley.png"))
B1=Button(text="meteo",command=Meteo).pack()
screen.mainloop()