from tkinter import*
from setting.settingAssistant import*
from setting.view import*
from setting.settingInternet import*
from setting.settingMeteo import*
from setting.settingTraduction import *
from src.varriable import*
from setting.settingSoftware import*

listMoteur = "google" , "duckduckgo" , "ecosia" , "qwant" , "bing"
    
def Setting():#fonction parametre
    ScreenPara = Toplevel()
    ScreenPara.title("Ryley: Parametre")
    ScreenPara.iconphoto(False,PhotoImage(file="image/Ryley.png"))
    ScreenPara.maxsize(700,700)
    ScreenPara.minsize(700,700)
    left = Frame(ScreenPara,width=200,height=700,bg=secondColor) 
    right = Frame(ScreenPara,width=500,height=700,bg=mainColor)
    #fonction
    def web():
        NoViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
        ParaWeb(right,ScreenPara,btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
    def assistant():
        NoViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
        Assistant(right,ScreenPara,btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
    def meteo():
        NoViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
        Meteo(right,ScreenPara,btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
    def trad():
        Trad(right,ScreenPara,btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
        NoViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
    def soft():
        NoViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
        Software(right,ScreenPara,btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
    #widget
    #label
    labelTitre = Label(left,text="Paramètre",font=("arial","30"),bg=secondColor,fg="white")
    #bouton
    btnAssistant = Button(left,text="Assistant",bg="white",fg="black",font=("arial","15"),command=assistant)
    btnInternet = Button(left,text="Internet",bg="white",fg="black",font=("arial","15"),command=web)
    btnMeteo = Button(left,text="Météo",bg="white",fg="black",font=("arial","15"),command=meteo)
    btnTraducteur = Button(left,text="Traducteur",bg="white",fg="black",font=("arial","15"),command=trad)
    btnSoftware = Button(left,text="Logiciel",bg="white",fg="black",font=("arial","15"),command=soft)
    
    #affichage
    left.pack(side="left")
    right.pack(side="right")
    ViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo,btnSoftware)
    labelTitre.place(x=5,y=5)
    ScreenPara.mainloop()