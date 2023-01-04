from tkinter import *
from function.JSON import*
from setting.view import*

MainColor = "white"
MainTextColor = "black"
SecondColor = "#1e23d3"
SecondTextColor = "white"

listLang = ["french","english","spanish"]
def Trad(cadre,screen,btn1,btn2,btn3,btn4):
    varLang = StringVar(screen)
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg=MainColor)
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4)
    def Affichage():
        labelTrad1.place(x=20,y=125)
        labelTrad2.place(x=20,y=225)
        labelTrad3.place(x=20,y=325)
        btnTrad1.place(x=265,y=125)
        btnTrad2.place(x=265,y=225)
        btnTrad3.place(x=265,y=325)
    def NoAffichage():
        labelTrad1.place_forget()
        labelTrad2.place_forget()
        labelTrad3.place_forget()
        btnTrad1.place_forget()
        btnTrad2.place_forget()
        btnTrad3.place_forget()
    def tradView():
        labelTrad4.place(x=20,y=125)
        menuLangue.place(x=100,y=230)
        btnTradValider.place(x=225,y=300)
    def NotradView():
        labelTrad4.place_forget()
        menuLangue.place_forget()
        btnTradValider.place_forget()
    def ExitTrad():
        NotradView()
        Affichage()
        btnTrad4.config(command=exit)
    def Traduction1():
        btnTrad4.config(command=ExitTrad)
        NoAffichage()
        tradView()
        def Valider():
            newLang = varLang.get()
            EcritureJSON("setting/config.json","lang0",newLang)
            ExitTrad()
        lang = lectureJSON("setting/config.json","lang0")
        if lang == "french":
            varLang.set(listLang[0])
        else :
            if lang == "english":
                varLang.set(listLang[1])
            else :
                varLang.set(listLang[2])
        btnTradValider.config(command=Valider)
    def Traduction2():
        btnTrad4.config(command=ExitTrad)
        NoAffichage()
        tradView()
        def Valider():
            newLang = varLang.get()
            EcritureJSON("setting/config.json","lang1",newLang)
            ExitTrad()
        lang = lectureJSON("setting/config.json","lang1")
        if lang == "french":
            varLang.set(listLang[0])
        else :
            if lang == "english":
                varLang.set(listLang[1])
            else :
                varLang.set(listLang[2])
        btnTradValider.config(command=Valider)
    def Traduction3():
        btnTrad4.config(command=ExitTrad)
        NoAffichage()
        tradView()
        def Valider():
            newLang = varLang.get()
            EcritureJSON("setting/config.json","lang2",newLang)
            ExitTrad()
        lang = lectureJSON("setting/config.json","lang2")
        if lang == "french":
            varLang.set(listLang[0])
        else :
            if lang == "english":
                varLang.set(listLang[1])
            else :
                varLang.set(listLang[2])
        btnTradValider.config(command=Valider)
        
   #declaration widget
    #btn
    btnTrad1 = Button(section,text="Modifier",bg=SecondColor,font=("arial","15"),fg=SecondTextColor,command=Traduction1)
    btnTrad2 = Button(section,text="Modifier",bg=SecondColor,font=("arial","15"),fg=SecondTextColor,command=Traduction2)
    btnTrad3 = Button(section,text="Modifier",bg=SecondColor,font=("arial","15"),fg=SecondTextColor,command=Traduction3)
    btnTrad4 = Button(section,text="Exit",bg=MainColor,font=("arial","15"),fg=MainTextColor,command=exit)
    btnTradValider = Button(section,text="Valider",bg=SecondColor,font=("arial","15"),fg=SecondTextColor)
    #Label
    labelIndication =Label(section,text="Modifier la langue de l'outil \nde traduction de l'assistant",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelTrad1 = Label(section,text="Langue du systeme",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelTrad2 = Label(section,text="Langue principale",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelTrad3 = Label(section,text="Langue secondaire",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    labelTrad4 = Label(section,text="Langue :",bg=MainColor,font=("arial","15"),fg=MainTextColor)
    #Menu deroulant 
    menuLangue = OptionMenu(section,varLang,*listLang)
    
    labelIndication.place(x=125,y=0)
    
    Affichage()
    
    btnTrad4.place(x=225,y=650)