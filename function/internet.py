import requests
import webbrowser
from tkinter import*
from function.JSON import*
from src.parole import*

MainColor = "white"
MainTextColor = "black"
SecondColor = "#1e23d3"
SecondTextColor = "white"

def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.com/search?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        liengoogle = urllink.url
        webbrowser.open(liengoogle)
def duckduckgoSearch(query):
    with requests.session() as c:
        url = 'https://duckduckgo.com/?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienduck = urllink.url
        webbrowser.open(lienduck)
def QwantSearch(query):
    with requests.session() as c:
        url = 'https://www.qwant.com/?l=fr&q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienQwant = urllink.url
        webbrowser.open(lienQwant)

def EcosiaSearch(query):
    with requests.session() as c:
        url = 'https://www.ecosia.org/search'
        query = {'q': query}
        urllink = requests.get(url,query)
        lienEcosia = urllink.url
        webbrowser.open(lienEcosia)
  
def bingSearch(query):
    with requests.session() as c:
        url = "https://www.bing.com/search"
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienbing = urllink.url
        webbrowser.open(lienbing)

def TestInternet():
    screenInternet = Toplevel()
    screenInternet.title("Ryley")
    screenInternet.maxsize(425,70)
    screenInternet.minsize(425,70)
    screenInternet.iconphoto(False,PhotoImage(file="image/Ryley.png"))
    screenInternet.config(bg=MainColor)
    try:
        _ = requests.get("https://duckduckgo.com",timeout=5)
        Info = Label(screenInternet,text="Internet disponible",font=("arial","20"),bg=MainColor,fg=MainTextColor).pack()
    except requests.ConnectionError :
        Info = Label(screenInternet,text="Internet non disponible",font=("arial","20"),bg=MainColor,fg=MainTextColor).pack()


def GrandRecherche(user,label,nom):
    speak("Que veux-tu rechercher "+ user +" ?",label,nom)
    screenRech = Toplevel()
    screenRech.config(bg=SecondColor)
    screenRech.title("Ryley : Grande Recherche")
    screenRech.maxsize(500,100)
    BarreRecher = Entry(screenRech,width=50)
    def Valider():
        recherche=BarreRecher.get()
        googleSearch(recherche)
        QwantSearch(recherche)
        duckduckgoSearch(recherche)
        EcosiaSearch(recherche)
        bingSearch(recherche)
        speak("Voici le résulat",label,nom)
    BoutonRecherche = Button(screenRech,text="Rechercher",bg=SecondColor,fg=SecondTextColor,command=Valider)
    BarreRecher.pack(side="left")
    BoutonRecherche.pack(side="right")

def Rechercheinternet():
    screenschearch=Toplevel()
    screenschearch.config(bg=SecondColor)
    screenschearch.title("Ryley : Recherche")
    screenschearch.maxsize(500,100)
    BarreRecher = Entry(screenschearch,width=50)
    def Valider():
        recherche=BarreRecher.get()
        moteur= lectureJSON("setting/config.json","nameMoteur")
        if moteur=="google":
            googleSearch(recherche)
        else :
            if moteur=="duckduckgo":
                duckduckgoSearch(recherche)
            else :
                if moteur=="ecosia":
                    EcosiaSearch(recherche)
                else :
                    if moteur=="bing":
                        bingSearch(recherche)
                    else :
                        QwantSearch(recherche)
            
    BoutonRecherche = Button(screenschearch,text="Rechercher",bg=SecondColor,fg=SecondTextColor,command=Valider)
    BarreRecher.pack(side="left")
    BoutonRecherche.pack(side="right")