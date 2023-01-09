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
        url = 'https://duckduckgo.com/?'
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
  
def braveSearch(query):
    with requests.session() as c:
        url = 'https://search.brave.com/search?q='
        urllink = requests.get(url+query+"&source=web")
        lienBrave = urllink.url
        webbrowser.open(lienBrave)

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


def GrandRecherche(recherche):
    i = 0
    while(i!=6):
        if (i==1) :
            googleSearch(recherche)
        else :
            if (i==2):                
                QwantSearch(recherche)
            else :
                if(i==3):
                    duckduckgoSearch(recherche)
                else :
                    if(i==4):
                        EcosiaSearch(recherche)
                    else :
                        if(i==5):
                            braveSearch(recherche)
        i = i + 1
