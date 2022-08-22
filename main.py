from multiprocessing.context import ForkContext
from tkinter import*
import webbrowser
import os
import datetime
import random
import requests
from tkinter.messagebox import showinfo
from translate import translate
import time
#Var
api_key="ecffd157b2cc9eacbd0d35a45c3dc047"
base_url="https://api.openweathermap.org/data/2.5/weather?"
Color = "#573ab6"
TextColor = "white"
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
    return 
def TestInternet():
    screenInternet = Toplevel()
    screenInternet.title("Ryley")
    screenInternet.maxsize(425,70)
    screenInternet.minsize(425,70)
    screenInternet.config(bg=Color)
    try:
        _ = requests.get("https://duckduckgo.com",timeout=5)
        Info = Label(screenInternet,text="Internet disponible",font=("arial","20"),bg=Color,fg=TextColor).pack()
    except requests.ConnectionError :
        Info = Label(screenInternet,text="Internet non disponible",font=("arial","20"),bg=Color,fg=TextColor).pack()
def Parametre():
    ScreenPara = Toplevel()
    def ParaAssistant():
        CadreAssistant.pack(side="right")
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
    ScreenPara.title("Ryley : Paramétre")
    ScreenPara.maxsize(500,500)
    ScreenPara.minsize(500,500)
    ScreenPara.config(bg=Color)
    LabelIndication = Label(ScreenPara,text="Paramétre",font=("arial","30"),bg=Color,fg=TextColor)
    #Cadre Para
    CadrePara = Frame(ScreenPara,bg="black",width=100,height=450)
    BoutonPara1 = Button(CadrePara,text="Assistant",bg=Color,fg=TextColor,command=ParaAssistant)
    #Cadre Assistant
    CadreAssistant = Frame(ScreenPara,bg=Color,width=350,height=400)
    BoutonAssistant1 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=ModifNom)
    BoutonAssistant2 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=ModifUser)
    Assistant1 = Label(CadreAssistant,text="Nom de l'assistant",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant2 = Label(CadreAssistant,text="Utilisateur",bg=Color,fg=TextColor,font=("arial","17"))
    #Affichage
    LabelIndication.pack()
    CadrePara.pack(side="left")
    #Cadre Para
    BoutonPara1.place(x="5",y="5")
    #Cadre Assistant
    Assistant1.place(x="5",y="5")
    BoutonAssistant1.place(x="250",y="5")
    Assistant2.place(x="5",y="55")
    BoutonAssistant2.place(x="250",y="55")
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
#Definition fenetre Tkinter
screen = Tk()
screen.title("Ryley")
screen.config(bg=Color)
screen.maxsize(500,600)
screen.minsize(500,600)
screen.iconphoto(False,PhotoImage(file="image/Ryley.png"))
#Menu
RyleyMenu = Menu(screen,bg="white",fg="black")
FichierMenu = Menu(RyleyMenu,tearoff=0)
FichierMenu.add_command(label="Paramétre",command=Parametre)
FichierMenu.add_command(label="Test Internet",command=TestInternet)
RyleyMenu.add_cascade(label="Fichier",menu=FichierMenu)
RyleyMenu.add_command(label="A propos")
screen.config(menu=RyleyMenu)
B1=Button(text="meteo",command=Meteo).pack()#Temporaire
#Code principal


screen.mainloop()