from tkinter import*
from src.systeme import*
from function.JSON import*
import time
from src.ryleySRC import *
from objet.actualiterMeteo.actuMeteo import*
from objet.gps.gps import *

api_key="ecffd157b2cc9eacbd0d35a45c3dc047"
base_url="https://api.openweathermap.org/data/2.5/weather?"


def Meteo(srcRyley:RyleySRC):
    
    varVille = lectureJSON("setting/config.json","ville")
    srcRyley.speak("Il fait "+meteo(ville(varVille).lat(),ville(varVille).long()).temperature()+"°C")
    time.sleep(1.5)
    srcRyley.speak("Le temps est "+meteo(ville(varVille).lat(),ville(varVille).long()).description())
    time.sleep(1.5)
    srcRyley.speak("Avec un taux d'humidité de "+meteo(ville(varVille).lat(),ville(varVille).long()).humiditer()+" %")
    time.sleep(1.5) 

def Resumeactu(srcRyley:RyleySRC):
    srcRyley.speak("Voyons voir, quoi de neuf aujourd'hui?")
    liste = Actualiter().recuperation()
    time.sleep(2)
    srcRyley.speak(liste[0])
    time.sleep(4)
    srcRyley.speak(liste[1])
    time.sleep(4)
    srcRyley.speak(liste[2])
    time.sleep(4)
    srcRyley.speak(liste[3])
    time.sleep(4)
    srcRyley.speak(liste[4])
    time.sleep(4)
    srcRyley.speak(liste[5])
    time.sleep(4)
    srcRyley.speak("Voici les actualités de ce moment.")
    