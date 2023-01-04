from cProfile import label
from tkinter import*
from tokenize import Name
from turtle import color
import webbrowser
import os
import datetime
import random
import requests
from tkinter.messagebox import showinfo
from translate import Translator
import time
from function.JSON import*
from setting.setting import*
#Var
api_key="ecffd157b2cc9eacbd0d35a45c3dc047"
base_url="https://api.openweathermap.org/data/2.5/weather?"
urlNew = "https://newsapi.org/v2/top-headlines?sources=google-news-fr"
keyNew = "3b43e18afcf945888748071d177b8513"
MainColor = "white"
MainTextColor = "black"
SecondColor = "#573ab6"
SecondTextColor = "white"
NomAssistant = lectureJSON("setting/config.json","nomAssistant")
User = lectureJSON("setting/config.json","user")
#Definition fenetre Tkinter
screen = Tk()
bgTOP = PhotoImage(file = "image/BGTop.png")
bgBOTTOM = PhotoImage(file = "image/BGBottom.png")
screen.title("Ryley")
screen.config(bg=MainColor)
screen.maxsize(500,600)
screen.minsize(500,600)
screen.iconphoto(False,PhotoImage(file="image/Ryley.png"))
top = Canvas( screen, width = 500,height = 400)
top.pack()
top.create_image( 0, 0, image = bgTOP, anchor = "nw")
bottom = Canvas( screen, width = 500,height = 200)
bottom.pack(side="bottom")
bottom.create_image( 0, 0, image = bgBOTTOM, anchor = "nw")
labelSpeak = Label(top,text=NomAssistant+":",bg=MainColor,fg=MainTextColor,font=("arial","14"))
#Fonction

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
def APropos():
    screenAPropos = Toplevel()
    screenAPropos.title("Ryley")
    screenAPropos.maxsize(425,170)
    screenAPropos.minsize(425,170)
    screenAPropos.iconphoto(False,PhotoImage(file="image/Ryley.png"))
    screenAPropos.config(bg=MainColor)
    Label(screenAPropos,text="Assistant Personnelle Ryley\nCréer par:\nSpeedyCreator\net\nWiruto2",font=("arial","20"),bg=MainColor,fg=MainTextColor).pack()

def Speak(text):
    labelSpeak.config(text=NomAssistant+": "+text)
    labelSpeak.update()
def Introduction():
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour <=5:
        Speak("Zzzz "+User+" Il faut peut etre dormir non?")
    if hour >= 6 and hour <= 9 :
        Speak("Hey "+User+" as-tu bien dormi?")
    if hour >= 10 and hour <= 12:
        Speak("Salut "+User+" comment ce passe ta matinée?")
    if hour >= 13 and hour <= 17:
        Speak("Alors "+User+" pret a travailler?")
    if hour >= 18 and hour <= 23:
        Speak("*baille* "+User+" ? Que fais tu si tard?")
def Meteo():
    varVille = lectureJSON("setting/config.json","ville")
    complete_url=base_url+"appid="+api_key+"&q="+varVille+"&lang=fr"+"&units=metric"
    reponse=requests.get(complete_url).json()
    if reponse["cod"]!="404":
        DICT=reponse["main"]
        temp=str(DICT["temp"])
        humidity=str(DICT["humidity"])
        meteodet=str(reponse["weather"][0]["description"])
        Speak("Il fait "+temp+"°C")
        time.sleep(2.5)
        Speak("Le temps est "+meteodet)
        time.sleep(3)
        Speak("Avec un taux d'humidité de "+humidity+"%")
def Resumeactu():
    def NetoyageActu(dictionnnaire):#Fonction qui permet de netoyer les donne recu par l'API
        Sujet = dictionnnaire["content"]
        Description = dictionnnaire["description"]
        URL= dictionnnaire["url"]
        Titre = dictionnnaire["title"]
        return Sujet,Description,URL,Titre  
    Speak("Voyons voir, quoi de neuf aujourd'hui?")
    time.sleep(2)
    completeURLNew = urlNew+"&pageSize=3"+"&apiKey="+keyNew
    article=requests.get(completeURLNew).json()["articles"]
    Sujet1,description1,url1,titre1=NetoyageActu(article[0])
    Sujet2,description2,url2,titre2=NetoyageActu(article[1])
    Sujet3,description3,url3,titre3=NetoyageActu(article[2])
    screenActu = Toplevel()
    screenActu.minsize(300,50)
    screenActu.config(bg=MainColor)
    labelActu = Label(screenActu,bg=MainColor,fg=MainTextColor,font=("arial","14"))
    Speak("Tadam! Voici une première actualité : ")
    labelActu.pack()
    labelActu.config(text=titre1)
    labelActu.update()
    time.sleep(2)
    Speak("Et voila la suite : ")
    labelActu.update()
    time.sleep(2)
    labelActu.config(text=titre2)
    labelActu.update()
    time.sleep(2)
    Speak("Efin : ")
    labelActu.update()
    time.sleep(2)
    labelActu.config(text=titre3)
    labelActu.update()
    time.sleep(2)
    labelActu.pack_forget()
    BoutonQuit = Button(screenActu,text="Quitter",command=screenActu.destroy,bg=MainColor,fg=MainTextColor,).pack()
def Rechercheninternet():
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
def Traduction():
    langue0=lectureJSON("setting/config.json","lang0")
    langue1=lectureJSON("setting/config.json","lang1")
    langue2=lectureJSON("setting/config.json","lang2")
    ScreenTrad=Tk()
    ScreenTrad.title("Ryley's Trad")
    ScreenTrad.maxsize(400,400)
    ScreenTrad.minsize(400,400)
    ScreenTrad.config(bg=SecondColor)
    labelInfo=Label(ScreenTrad,text="Resultat",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    trad=Entry(ScreenTrad,width=45)
    def L0versL1():
        mot = str(trad.get())
        translator= Translator(from_lang=langue0,to_lang=langue1)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L0versL2():
        mot = str(trad.get())
        translator= Translator(from_lang=langue0,to_lang=langue2)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L1versL0():
        mot = str(trad.get())
        translator= Translator(from_lang=langue1,to_lang=langue0)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L1versL2():
        mot = str(trad.get())
        translator= Translator(from_lang=langue1,to_lang=langue2)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L2versL0():
        mot = str(trad.get())
        translator= Translator(from_lang=langue2,to_lang=langue0)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L2versL1():
        mot = str(trad.get())
        translator= Translator(from_lang=langue2,to_lang=langue1)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    bouttonTraduction=Button(ScreenTrad,text="Traduire",bg=SecondColor,fg=SecondTextColor)
    def Mode1():
        bouttonTraduction.config(command=L0versL1)
    def Mode2():
        bouttonTraduction.config(command=L1versL0)
    def Mode3():
        bouttonTraduction.config(command=L0versL2)
    def Mode4():
        bouttonTraduction.config(command=L2versL0)
    def Mode5():
        bouttonTraduction.config(command=L1versL2)
    def Mode6():
        bouttonTraduction.config(command=L2versL1)
    
    MenuTrad = Menu(ScreenTrad,bg="white")
    Choix = Menu(MenuTrad,tearoff=0)
    Choix.add_command(label="Langue par défault vers Langue 1",command=Mode1)
    Choix.add_command(label="Langue 1 vers Langue par défault",command=Mode2)
    Choix.add_command(label="Langue par défault vers Langue 2",command=Mode3)
    Choix.add_command(label="Langue 2 vers Langue par défault",command=Mode4)
    Choix.add_command(label="Langue 1 vers Langue 2",command=Mode5)
    Choix.add_command(label="Langue 2 vers Langue 1",command=Mode6)
    MenuTrad.add_cascade(label = "Traduction",menu=Choix)
    ScreenTrad.config(menu=MenuTrad)
    labelInfo.place(x="5",y="25")
    trad.place(relx=.5,rely=.5,anchor ="center")
    bouttonTraduction.pack(side="bottom")
    ScreenTrad.mainloop()
def GrandRecherche():
    Speak("Que veux-tu rechercher "+Name+" ?")
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
        Speak("Voici le résulat")
    BoutonRecherche = Button(screenRech,text="Rechercher",bg=SecondColor,fg=SecondTextColor,command=Valider)
    BarreRecher.pack(side="left")
    BoutonRecherche.pack(side="right")
#Menu
RyleyMenu = Menu(screen,bg="white",fg="black")
FichierMenu = Menu(RyleyMenu,tearoff=0)
FichierMenu.add_command(label="Paramétre",command=Setting)
FichierMenu.add_command(label="Test Internet",command=TestInternet)
RyleyMenu.add_cascade(label="Fichier",menu=FichierMenu)
RyleyMenu.add_command(label="A propos",command=APropos)
screen.config(menu=RyleyMenu)
#Code principal
Introduction()
BarreR = Entry(bottom,width=50)
def Interaction():
    requete=str(BarreR.get())
    gDrive = lectureJSON("setting/config.json","lienDrive")
    lienEDT = lectureJSON("setting/config.json","lienEDT")
    lienAgenda = lectureJSON("setting/config.json","lienAngenda")
    LienSite1 = lectureJSON("setting/config.json","lienSite1")
    NameSite1 = lectureJSON("setting/config.json","NameSite1")
    LienSite2 = lectureJSON("setting/config.json","lienSite2")
    NameSite2 = lectureJSON("setting/config.json","NameSite2")
    LienSite3 = lectureJSON("setting/config.json","lienSite3")
    NameSite3 = lectureJSON("setting/config.json","NameSite3")
    if "quit" in requete:
        screen.quit()
    if "meteo" in requete:
        Meteo()
    if "traduction" in requete or "Traduction" in requete or "trad" in requete:
        Traduction()
    if "Drive" in requete or "Google Drive" in requete or "drive" in requete:
        Speak("Voici Google Drive ;)")
        time.sleep(1.75)
        webbrowser.open(gDrive)
    if "agenda" in requete or "taff" in requete or "devoirs" in requete or "devoir" in requete:
        Speak("Voila ce que tu as à faire : ")
        time.sleep(1.75)
        webbrowser.open(lienAgenda)
    if "emploi du temps" in requete or "edt" in requete or "planning" in requete or "emploi du tps" in requete :
        Speak("Tiens, ton planning des jours à venir :")
        time.sleep(1.75)
        webbrowser.open(lienEDT)
    if NameSite1 in requete:
        Speak("Voila ! ")
        time.sleep(1.25)
        webbrowser.open(LienSite1)
    if NameSite2 in requete:
        Speak("Et voici ! ")
        time.sleep(1.25)
        webbrowser.open(LienSite2)
    if NameSite3 in requete:
        Speak("Tiens ! ")
        time.sleep(1.25)
        webbrowser.open(LienSite3)
    if "actu" in requete or "actualité" in requete or "news" in requete :
        Resumeactu()
    if "Grecherche" in requete:
        GrandRecherche()
    if "Recherche" in requete or "recherche" in requete:
        Rechercheninternet()
BoutonEnvoyer=Button(bottom,text="Envoyer",command=Interaction,bg=SecondColor,fg=SecondTextColor)
#Affichage
labelSpeak.place(x="10",y="300")
BarreR.place(x="0",y="130")
BoutonEnvoyer.place(x="415",y="125")
#Fin de la boucle
screen.mainloop()