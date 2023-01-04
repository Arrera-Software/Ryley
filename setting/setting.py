from tkinter import*
from setting.assistant import*
from setting.view import*
from setting.internet import*
from setting.meteo import*
from setting.traduction import *
from varriable import*

listMoteur = "google" , "duckduckgo" , "ecosia" , "qwant" , "bing"
    
def Setting():#fonction parametre
    ScreenPara = Toplevel()
    ScreenPara.title("Ryley: Parametre")
    ScreenPara.maxsize(700,700)
    ScreenPara.minsize(700,700)
    left = Frame(ScreenPara,width=200,height=700,bg=secondColor) 
    right = Frame(ScreenPara,width=500,height=700,bg=mainColor)
    #fonction
    def web():
        NoViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo)
        ParaWeb(right,ScreenPara,btnAssistant,btnInternet,btnTraducteur,btnMeteo)
    def assistant():
        NoViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo)
        Assistant(right,ScreenPara,btnAssistant,btnInternet,btnTraducteur,btnMeteo)
    def meteo():
        NoViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo)
        Meteo(right,ScreenPara,btnAssistant,btnInternet,btnTraducteur,btnMeteo)
    def trad():
        Trad(right,ScreenPara,btnAssistant,btnInternet,btnTraducteur,btnMeteo)
        NoViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo)
    #widget
    #label
    labelTitre = Label(left,text="Paramètre",font=("arial","30"),bg=secondColor,fg="white")
    #bouton
    btnAssistant = Button(left,text="Assistant",bg="white",fg="black",font=("arial","15"),command=assistant)
    btnInternet = Button(left,text="Internet",bg="white",fg="black",font=("arial","15"),command=web)
    btnMeteo = Button(left,text="Météo",bg="white",fg="black",font=("arial","15"),command=meteo)
    btnTraducteur = Button(left,text="Traducteur",bg="white",fg="black",font=("arial","15"),command=trad)

    #affichage
    left.pack(side="left")
    right.pack(side="right")
    ViewBTN(btnAssistant,btnInternet,btnTraducteur,btnMeteo)
    labelTitre.place(x=5,y=5)
    ScreenPara.mainloop()