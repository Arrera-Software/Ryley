from tkinter import *
from function.JSON import*
from setting.view import*
from varriable import*

listMoteur=["duckduckgo","google","qwant","ecosia"]
listLienMoteur=["https://duckduckgo.com/","https://www.google.com/","https://www.qwant.com/","https://www.ecosia.org/"]


def ParaWeb(cadre,screen,btn1,btn2,btn3,btn4):
    varMoteur = StringVar(screen)
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg=mainColor)
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4)
    def Affichage():
        labelWeb1.place(x=20,y=125)
        labelWeb2.place(x=20,y=185)
        labelWeb3.place(x=20,y=245)
        labelWeb4.place(x=20,y=305)
        labelWeb5.place(x=20,y=365)
        labelWeb6.place(x=20,y=425)
        labelWeb7.place(x=20,y=485)
        
        btnWeb1.place(x=265,y=125)
        btnWeb2.place(x=265,y=185)
        btnWeb3.place(x=265,y=245)
        btnWeb4.place(x=265,y=305)
        btnWeb5.place(x=265,y=365)
        btnWeb6.place(x=265,y=425)
        btnWeb7.place(x=265,y=485)
    def NoAffichage():
        labelWeb1.place_forget()
        labelWeb2.place_forget()
        labelWeb3.place_forget()
        labelWeb4.place_forget()
        labelWeb5.place_forget()
        labelWeb6.place_forget()
        labelWeb7.place_forget()
    
        btnWeb1.place_forget()
        btnWeb2.place_forget()
        btnWeb3.place_forget()
        btnWeb4.place_forget()
        btnWeb5.place_forget()
        btnWeb6.place_forget()
        btnWeb7.place_forget()
    def MoteurView():
        labelWeb8.place(x=20,y=125)
        menuGenre.place(x=100,y=230)
        btnValiderWeb.place(x=225,y=300)
    def NoMoteurView():
        labelWeb8.place_forget()
        menuGenre.place_forget()
        btnValiderWeb.place_forget()
    def ExitMoteur():
        NoMoteurView()
        btnWeb8.config(command=exit)
        Affichage()
    def Moteur():
        btnWeb8.config(command=ExitMoteur)
        def valider():
            newMoteur = varMoteur.get()
            EcritureJSON("setting/config.json","nameMoteur",newMoteur)
            if newMoteur == "duckduckgo" :
                EcritureJSON("setting/config.json","lienMoteur",listLienMoteur[0])
            else :
                if newMoteur == "google" :
                    EcritureJSON("setting/config.json","lienMoteur",listLienMoteur[1])
                else :
                    if newMoteur == "qwant" :
                        EcritureJSON("setting/config.json","lienMoteur",listLienMoteur[2])
                    else :
                        EcritureJSON("setting/config.json","lienMoteur",listLienMoteur[3])
                
            ExitMoteur()
        btnValiderWeb.config(command=valider)
        moteur = lectureJSON("setting/config.json","nameMoteur")
        if moteur == "duckduckgo" :
            varMoteur.set(listMoteur[0])
        else :
            if moteur == "google" :
                varMoteur.set(listMoteur[1])
            else :
                if moteur == "qwant" :
                    varMoteur.set(listMoteur[2])
                else :
                    varMoteur.set(listMoteur[3])

        NoAffichage()
        MoteurView()
    def LienView():
        labelWeb9.place(x=20,y=125)
        entryLien.place(x=100,y=230)
        btnValiderWeb.place(x=225,y=300)
    def NoLienView():
        labelWeb9.place_forget()
        entryLien.place_forget()
        btnValiderWeb.place_forget()
    def ExitLien():
        NoLienView()
        Affichage()
        btnWeb8.config(command=exit)
    def Lien1():
        NoAffichage()
        btnWeb8.config(command=ExitLien)
        def Valider():
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","lienAngenda",newLien)
            ExitLien()
        btnValiderWeb.config(command=Valider)
        LienView()
    def Lien2():
        NoAffichage()
        btnWeb8.config(command=ExitLien)
        def Valider():
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","lienDrive",newLien)
            ExitLien()
        btnValiderWeb.config(command=Valider)
        LienView()
    def Lien3():
        NoAffichage()
        btnWeb8.config(command=ExitLien)
        def Valider():
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","lienEDT",newLien)
            ExitLien()
        btnValiderWeb.config(command=Valider)
        LienView()
    def NoViewApp():
        entryLien2.place_forget()
        entryName.place_forget()
        btnValiderWeb.place_forget()
        labelWeb10.place_forget()
        labelWeb11.place_forget()
    def ViewApp():
        labelWeb10.place(x=20,y=125)
        labelWeb11.place(x=20,y=225)
        btnValiderWeb.place(x=225,y=300)
        entryName.place(x=100,y=130)
        entryLien2.place(x=100,y=230)
    def ExitModif():
        btnWeb8.config(command=exit)
        NoViewApp()
        Affichage()
    def App1():
        btnWeb8.config(command=ExitModif)
        def valider1():
            newName = entryName.get()
            newLien = entryLien2.get()
            EcritureJSON("setting/config.json","NameSite1",newName)
            EcritureJSON("setting/config.json","lienSite1",newLien)
            ExitModif()
        btnValiderWeb.config(command=valider1)
        NoAffichage()
        ViewApp()
        
    def App2():
        btnWeb8.config(command=ExitModif)
        def valider1():
            newName = entryName.get()
            newLien = entryLien2.get()
            EcritureJSON("setting/config.json","NameSite2",newName)
            EcritureJSON("setting/config.json","lienSite2",newLien)
            ExitModif()
        btnValiderWeb.config(command=valider1)
        NoAffichage()
        ViewApp()
    
    def App3():
        btnWeb8.config(command=ExitModif)
        def valider1():
            newName = entryName.get()
            newLien = entryLien2.get()
            EcritureJSON("setting/config.json","NameSite3",newName)
            EcritureJSON("setting/config.json","lienSite3",newLien)
            ExitModif()
        btnValiderWeb.config(command=valider1)
        NoAffichage()
        ViewApp()
    #declaration widget
    #btn
    btnWeb1 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=Moteur)
    btnWeb2 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=Lien1)
    btnWeb3 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=Lien2)
    btnWeb4 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=Lien3)
    btnWeb5 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=App1)
    btnWeb6 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=App2)
    btnWeb7 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=App3)
    btnWeb8 = Button(section,text="Exit",bg=mainColor,font=("arial","15"),fg=mainTextColor,command=exit)
    btnValiderWeb = Button(section,text="Valider",bg=secondColor,font=("arial","15"),fg=secondTextColor)
    #Label
    labelIndication =Label(section,text="Changer les lien de vos site\n qui vous sont utile",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb1 = Label(section,text="Moteur de recherche",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb2 = Label(section,text="Lien de l'agenda",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb3 = Label(section,text="Lien Stokage Cloud",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb4 = Label(section,text="Lien emplois du temps",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb5 = Label(section,text="Site favorie 1",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb6 = Label(section,text="Site favorie 2",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb7 = Label(section,text="Site favorie 3",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb8 = Label(section,text="Choisissez-votre moteur de recherche préférer",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb9 = Label(section,text="Lien :",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelWeb10  = Label(section,text="Nom : ",bg=mainColor,font=("arial","15"),fg=mainTextColor) 
    labelWeb11  = Label(section,text="Lien : ",bg=mainColor,font=("arial","15"),fg=mainTextColor) 
    #entry
    entryLien = Entry(section,width=30,font=("arial","15"))
    entryLien2 = Entry(section,width=30,font=("arial","15"))
    entryName = Entry(section,width=30,font=("arial","15"))
    #Menu deroulant 
    menuGenre = OptionMenu(section,varMoteur,*listMoteur)
    
    labelIndication.place(x=125,y=0)
    
    Affichage()
    
    btnWeb8.place(x=225,y=650)
    