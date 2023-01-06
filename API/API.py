from tkinter import*
from varriable import*
from function.JSON import*
import requests
import time
from src.parole import*

api_key="ecffd157b2cc9eacbd0d35a45c3dc047"
base_url="https://api.openweathermap.org/data/2.5/weather?"
urlNew = "https://newsapi.org/v2/top-headlines?sources=google-news-fr"
keyNew = "3b43e18afcf945888748071d177b8513"

def Meteo(label,nom):
    varVille = lectureJSON("setting/config.json","ville")
    reponse=requests.get(base_url+"appid="+api_key+"&q="+varVille+"&lang=fr"+"&units=metric").json()
    if reponse["cod"]!="404":
        dictionnaire=reponse["main"]
        temp=str(dictionnaire["temp"])
        humidity=str(dictionnaire["humidity"])
        meteodet=str(reponse["weather"][0]["description"])
        speak("Il fait "+temp+"°C",label,nom)
        time.sleep(1.5)
        speak("Le temps est "+meteodet,label,nom)
        time.sleep(1.5)
        speak("Avec un taux d'humidité de "+humidity+" %",label,nom)
def NetoyageActu(dictionnnaire):#Fonction qui permet de netoyer les donne recu par l'API
    Titre = dictionnnaire["title"]
    return Titre  
def Resumeactu(label,nom):
    speak("Voyons voir, quoi de neuf aujourd'hui?",label,nom)
    time.sleep(2)
    article=requests.get(urlNew+"&pageSize=3"+"&apiKey="+keyNew).json()["articles"]
    titre1=NetoyageActu(article[0])
    titre2=NetoyageActu(article[1])
    titre3=NetoyageActu(article[2])
    screenActu = Toplevel()
    screenActu.minsize(300,50)
    screenActu.config(bg=mainColor)
    labelActu = Label(screenActu,bg=mainColor,fg=mainTextColor,font=("arial","14"))
    speak("Tadam! Voici une première actualité : ",label,nom)
    labelActu.pack()
    labelActu.config(text=titre1)
    labelActu.update()
    time.sleep(2)
    speak("Et voila la suite : ",label,nom)
    labelActu.update()
    time.sleep(2)
    labelActu.config(text=titre2)
    labelActu.update()
    time.sleep(2)
    speak("Efin : ",label,nom)
    labelActu.update()
    time.sleep(2)
    labelActu.config(text=titre3)
    labelActu.update()
    time.sleep(3)
    labelActu.pack_forget()
    screenActu.destroy()
    speak("Voici les information que je peux vous donner",label,nom)