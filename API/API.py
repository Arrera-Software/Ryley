from tkinter import*
from src.varriable import*
from function.JSON import*
import requests
import time
from src.ryleySRC import *
from objet.actualiterMeteo.actuMeteo import*
from objet.gps.gps import *

api_key="ecffd157b2cc9eacbd0d35a45c3dc047"
base_url="https://api.openweathermap.org/data/2.5/weather?"


def Meteo(label,nom):
    
    varVille = lectureJSON("setting/config.json","ville")
    RyleySRC.speak("Il fait "+meteo(ville(varVille).lat(),ville(varVille).long()).temperature()+"°C",label,nom)
    time.sleep(1.5)
    RyleySRC.speak("Le temps est "+meteo(ville(varVille).lat(),ville(varVille).long()).description(),label,nom)
    time.sleep(1.5)
    RyleySRC.speak("Avec un taux d'humidité de "+meteo(ville(varVille).lat(),ville(varVille).long()).humiditer()+" %",label,nom)
    time.sleep(1.5) 

def Resumeactu(label,nom):
    RyleySRC.speak("Voyons voir, quoi de neuf aujourd'hui?",label,nom)
    liste = Actualiter().recuperation()
    time.sleep(2)
    RyleySRC.speak(liste[0],label,nom)
    time.sleep(4)
    RyleySRC.speak(liste[1],label,nom)
    time.sleep(4)
    RyleySRC.speak(liste[2],label,nom)
    time.sleep(4)
    RyleySRC.speak(liste[3],label,nom)
    time.sleep(4)
    RyleySRC.speak(liste[4],label,nom)
    time.sleep(4)
    RyleySRC.speak(liste[5],label,nom)
    time.sleep(4)
    RyleySRC.speak("Voici les actualités de ce moment.",label,nom)
    