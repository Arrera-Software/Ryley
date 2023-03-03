from tkinter import *
from function.JSON import*
from setting.view import*
from src.varriable import*

def Meteo(cadre,screen,btn1,btn2,btn3,btn4,btn5):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg=mainColor)
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5)
    def Affichage():
        labelMeteo1.place(x=20,y=125)
    
        btnMeteo1.place(x=195,y=125)
    def NoAffichage():
        labelMeteo1.place_forget()
        btnMeteo1.place_forget()
    def MeteoView():
        labelMeteo6.place(x=20,y=125)
        entryVille.place(x=100,y=230)
        btnMeteoValider.place(x=225,y=300)
    def NoMeteoView():
        labelMeteo6.place_forget()
        entryVille.place_forget()
        btnMeteoValider.place_forget()
    def ExitModif():
        btnMeteo6.config(command=exit)
        Affichage()
        NoMeteoView()
    def Meteo1():
        NoAffichage()
        btnMeteo6.config(command=ExitModif)
        def valider():
            newVille = entryVille.get()
            EcritureJSON("setting/config.json","ville",newVille)
            ExitModif()
        btnMeteoValider.config(command=valider)
        MeteoView()
   #declaration widget
    #btn
    btnMeteo1 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=Meteo1)
    btnMeteo6 = Button(section,text="Exit",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=exit)
    btnMeteoValider = Button(section,text="Valider",bg=secondColor,font=("arial","15"),fg=secondTextColor)
    #Label
    labelIndication =Label(section,text="Changer la localisation \nde vos lieu",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelMeteo1 = Label(section,text="Lieu de Meteo",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelMeteo6 = Label(section,text="Nom de la ville :",bg=mainColor,font=("arial","15"),fg=mainTextColor) 
    #entry
    entryVille = Entry(section,width=30,font=("arial","15"))
    
    labelIndication.place(x=125,y=0)
    
    Affichage()
    
    btnMeteo6.place(x=225,y=625)