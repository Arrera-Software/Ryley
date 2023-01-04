from tkinter import *
from function.JSON import*
from setting.view import*

MainColor = "white"
MainTextColor = "black"
SecondColor = "#1e23d3"
SecondTextColor = "white"

def Meteo(cadre,screen,btn1,btn2,btn3,btn4):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg=MainColor)
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4)
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
    btnMeteo1 = Button(section,text="Modifier",bg=SecondColor,font=("arial","15"),fg=SecondTextColor,command=Meteo1)
    btnMeteo6 = Button(section,text="Exit",bg=SecondColor,font=("arial","15"),fg=SecondTextColor,command=exit)
    btnMeteoValider = Button(section,text="Valider",bg=SecondColor,font=("arial","15"),fg=SecondTextColor)
    #Label
    labelIndication =Label(section,text="Changer la localisation \nde vos lieu",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelMeteo1 = Label(section,text="Lieu de Meteo",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelMeteo6 = Label(section,text="Nom de la ville :",bg=MainColor,font=("arial","15"),fg=MainTextColor) 
    #entry
    entryVille = Entry(section,width=30,font=("arial","15"))
    
    labelIndication.place(x=125,y=0)
    
    Affichage()
    
    btnMeteo6.place(x=225,y=625)