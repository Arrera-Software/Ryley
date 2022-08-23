from tkinter import*
import webbrowser
import os
import datetime
import random
import requests
from tkinter.messagebox import showinfo
from translate import translate
import time
#Fonction
def Ecriture(file,text):#Fonction d'écriture sur un fichier texte
    doc = open(file,"w")
    doc.truncate()
    doc.write(text)
    doc.close()
    return text,file
def Lecture(file):#Fonction de lecture d'un fichier texte et stokage dans une varriable
    fichier = open(file,"r")
    contenu= fichier.readlines()[0]
    fichier.close()
    return contenu
#Var
api_key="ecffd157b2cc9eacbd0d35a45c3dc047"
base_url="https://api.openweathermap.org/data/2.5/weather?"
Color = "#573ab6"
TextColor = "white"
NomAssistant = str(Lecture("Config/Nom.txt"))
User = str(Lecture("Config/User.txt"))
#Definition fenetre Tkinter
screen = Tk()
screen.title("Ryley")
screen.config(bg=Color)
screen.maxsize(500,600)
screen.minsize(500,600)
screen.iconphoto(False,PhotoImage(file="image/Ryley.png"))
Ecranretour=Frame(screen,bg=Color,width=450,height=400)
labelSpeak = Label(Ecranretour,text=NomAssistant+":",bg=Color,fg=TextColor,font=("arial","13"))
labelSpeak.place(x="0",y="0")
#Fonction
def TestInternet():
    screenInternet = Toplevel()
    screenInternet.title("Ryley")
    screenInternet.maxsize(425,70)
    screenInternet.minsize(425,70)
    screenInternet.iconphoto(False,PhotoImage(file="image/Ryley.png"))
    screenInternet.config(bg=Color)
    try:
        _ = requests.get("https://duckduckgo.com",timeout=5)
        Info = Label(screenInternet,text="Internet disponible",font=("arial","20"),bg=Color,fg=TextColor).pack()
    except requests.ConnectionError :
        Info = Label(screenInternet,text="Internet non disponible",font=("arial","20"),bg=Color,fg=TextColor).pack()
def Parametre():
    ScreenPara = Toplevel()
    def ParaAssistant():
        CadreMeteo.pack_forget()
        CadreLang.pack_forget()
        CadreAssistant.pack(side="right")
    def ParaMeteo():
        CadreAssistant.pack_forget()
        CadreLang.pack_forget()
        CadreLien.pack_forget()
        CadreMeteo.pack(side="right")
    def ParaLang():
        CadreMeteo.pack_forget()
        CadreAssistant.pack_forget()
        CadreLien.pack_forget()
        CadreLang.pack(side="right")
    def ParaLien():
        CadreMeteo.pack_forget()
        CadreLang.pack_forget()
        CadreAssistant.pack_forget()
        CadreLien.pack_forget()
        CadreLien.pack(side="right")
    def FoncModif(file):
        Contenu = Lecture(file)
        ScreenModif = Toplevel()
        ScreenModif.maxsize(300,150)
        ScreenModif.minsize(300,150)
        ScreenModif.wait_visibility(ScreenModif)
        ScreenModif.wm_attributes('-alpha',0.9)
        ScreenModif.config(bg=Color)
        LabelContenu = Label(ScreenModif,text=Contenu,font=("arial","20"),bg=Color,fg=TextColor)
        entry = Entry(ScreenModif)
        def Modif():
            Var = str(entry.get())
            Ecriture(file,Var)
            ScreenModif.destroy()
        Modif = Button(ScreenModif,text="Modifier",bg=Color,fg=TextColor,command=Modif).pack(side="right",anchor="s")
        LabelContenu.pack()
        entry.pack(side="left",anchor="s")
    def ModifUser():
        FoncModif("Config/User.txt")
    def ModifNom():
        FoncModif("Config/Nom.txt")
    def MeteoChange1():
        FoncModif("Config/Ville.txt")
    def LangChange1():
        FoncModif("Config/Lang1.txt")
    def LangChange2():
        FoncModif("Config/Lang2.txt")
    def LienChange1():
        FoncModif("Config/GDrive.txt")
    def LienChange2():
        FoncModif("Config/EDT.txt")
    def LienChange3():
        FoncModif("Config/Agenda.txt")
    def LienChange4():
        FoncModif("Config/Site1.txt")
    def LienChange5():
        FoncModif("Config/Site2.txt")
    def LienChange6():
        FoncModif("Config/Site3.txt")
    ScreenPara.title("Ryley : Paramétre")
    ScreenPara.maxsize(500,500)
    ScreenPara.minsize(500,500)
    ScreenPara.iconphoto(False,PhotoImage(file="image/Ryley.png"))
    ScreenPara.config(bg=Color)
    LabelIndication = Label(ScreenPara,text="Paramétre",font=("arial","30"),bg=Color,fg=TextColor)
    #Cadre Para
    CadrePara = Frame(ScreenPara,bg="black",width=100,height=450)
    BoutonPara1 = Button(CadrePara,text="Assistant",bg=Color,fg=TextColor,command=ParaAssistant)
    BoutonPara2= Button(CadrePara,text="Méteo",bg=Color,fg=TextColor,command=ParaMeteo)
    BoutonPara3= Button(CadrePara,text="Traduction",bg=Color,fg=TextColor,command=ParaLang)
    BoutonPara4 = Button(CadrePara,text="Lien",bg=Color,fg=TextColor,command = ParaLien)
    #Cadre Assistant
    CadreAssistant = Frame(ScreenPara,bg=Color,width=350,height=400)
    BoutonAssistant1 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=ModifNom)
    BoutonAssistant2 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=ModifUser)
    Assistant1 = Label(CadreAssistant,text="Nom de l'assistant",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant2 = Label(CadreAssistant,text="Utilisateur",bg=Color,fg=TextColor,font=("arial","17"))
    #Cadre Meteo
    CadreMeteo = Frame(ScreenPara,bg=Color,width=350,height=400)
    Meteo1 = Label(CadreMeteo,text="Lieu météo",bg=Color,fg=TextColor,font=("arial","20"))
    BoutonMeteo1 = Button(CadreMeteo,text="Change",bg=Color,fg=TextColor,command=MeteoChange1,font=("arial","15"))
    #Cadre Lang
    CadreLang = Frame(ScreenPara,bg=Color,width=350,height=400)
    Lang1 = Label(CadreLang,text="Langue Principal",bg=Color,fg=TextColor,font=("arial","20"))
    Lang2 = Label(CadreLang,text="Deuxiéme Langue",bg=Color,fg=TextColor,font=("arial","20"))
    BoutonLang1 = Button(CadreLang,text="Change",bg=Color,fg=TextColor,command=LangChange1,font=("arial","15"))
    BoutonLang2 = Button(CadreLang,text="Change",bg=Color,fg=TextColor,command=LangChange2,font=("arial","15"))
    #Cadre Lien
    CadreLien = Frame(ScreenPara,bg=Color,width=350,height=400)
    Lien1  = Label(CadreLien,text="Google Drive",bg=Color,fg=TextColor,font=("arial","20"))
    Lien2  = Label(CadreLien,text="Emplois du Temps",bg=Color,fg=TextColor,font=("arial","20"))
    Lien3  = Label(CadreLien,text="Lien Angenda",bg=Color,fg=TextColor,font=("arial","20"))
    Lien4  = Label(CadreLien,text="Site internet 1",bg=Color,fg=TextColor,font=("arial","20"))
    Lien5  = Label(CadreLien,text="Site internet 2",bg=Color,fg=TextColor,font=("arial","20"))
    Lien6  = Label(CadreLien,text="Site internet 3",bg=Color,fg=TextColor,font=("arial","20"))
    BoutonLien1 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,command=LienChange1,font=("arial","15"))
    BoutonLien2 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,command=LienChange2,font=("arial","15"))
    BoutonLien3 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,command=LienChange3,font=("arial","15"))
    BoutonLien4 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,command=LienChange4,font=("arial","15"))
    BoutonLien5 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,command=LienChange5,font=("arial","15"))
    BoutonLien6 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,command=LienChange6,font=("arial","15"))
    #Affichage
    LabelIndication.pack()
    CadrePara.pack(side="left")
    #Cadre Para
    BoutonPara1.place(x="5",y="5")
    BoutonPara2.place(x="10",y="85")
    BoutonPara3.place(x="2",y="165")
    BoutonPara4.place(x="10",y="245")
    #Cadre Assistant
    Assistant1.place(x="5",y="5")
    BoutonAssistant1.place(x="250",y="5")
    Assistant2.place(x="5",y="55")
    BoutonAssistant2.place(x="250",y="55")
    #Cadre Meteo
    Meteo1.place(x="5",y="5")
    BoutonMeteo1.place(x="250",y="5")
    #Cadre Lang
    Lang1.place(x="5",y="5")
    BoutonLang1.place(x="250",y="5")
    Lang2.place(x="5",y="55")
    BoutonLang2.place(x="250",y="55")
    #Cadre lien
    Lien1.place(x="5",y="5")
    BoutonLien1.place(x="250",y="5")
    Lien2.place(x="5",y="55")
    BoutonLien2.place(x="250",y="55")
    Lien3.place(x="5",y="105")
    BoutonLien3.place(x="250",y="105")
    Lien4.place(x="5",y="155")
    BoutonLien4.place(x="250",y="155")
    Lien5.place(x="5",y="205")
    BoutonLien5.place(x="250",y="205")
    Lien6.place(x="5",y="255")
    BoutonLien6.place(x="250",y="255")
def Speak(text):
    labelSpeak.config(text=NomAssistant+": "+text)
    labelSpeak.update()
def Introduction():
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour <=5:
        Speak("Zzzz "+User+" Il faut peut etre dormir non?")
    if hour >= 6 and hour <= 9 :
        Speak("Hey "+User+" as-tu bien dormis?")
    if hour >= 10 and hour <= 12:
        Speak("Salut "+User+" comment ce passe ta matinée?")
    if hour >= 13 and hour <= 17:
        Speak("Alors "+User+" pret a travailler?")
    if hour >= 18 and hour <= 23:
        Speak("*baille* "+User+" ? Que fait tu si tard?")
def Meteo():
    fileVille=open("Config/Ville.txt","r")
    varVille=str(fileVille.readlines()[0])
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
#Menu
RyleyMenu = Menu(screen,bg="white",fg="black")
FichierMenu = Menu(RyleyMenu,tearoff=0)
FichierMenu.add_command(label="Paramétre",command=Parametre)
FichierMenu.add_command(label="Test Internet",command=TestInternet)
RyleyMenu.add_cascade(label="Fichier",menu=FichierMenu)
RyleyMenu.add_command(label="A propos")
screen.config(menu=RyleyMenu)
#Code principal
Introduction()
BarreR = Entry(screen,width=50)
def Interaction():
    requete=str(BarreR.get())
    NomAssistant = str(Lecture("Config/Nom.txt"))
    User = str(Lecture("Config/User.txt"))
    if "quit" in requete:
        screen.quit()
    if "meteo" in requete:
        Meteo()
BoutonEnvoyer=Button(text="Envoyer",command=Interaction,bg=Color,fg=TextColor)
Ecranretour.place(relx=.5,rely=.5,anchor ="center")
BarreR.pack(side="left",anchor="s")
BoutonEnvoyer.pack(side="right",anchor="s")
screen.mainloop()