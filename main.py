from tkinter import*
import webbrowser
import os
import datetime
import random
import requests
from tkinter.messagebox import showinfo
from translate import Translator
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
MainColor = "white"
MainTextColor = "black"
SecondColor = "#573ab6"
SecondTextColor = "white"
NomAssistant = str(Lecture("Config/Nom.txt"))
User = str(Lecture("Config/User.txt"))
listMoteur = "google" , "duckduckgo" , "ecosia" , "qwant" , "bing"
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
def Parametre():
    ScreenPara = Toplevel()
    def ParaAssistant():
        CadreMeteo.pack_forget()
        CadreLang.pack_forget()
        CadreLien.pack_forget()
        CadreMoteur.pack_forget()
        CadreAssistant.pack(side="right")
    def ParaMeteo():
        CadreAssistant.pack_forget()
        CadreLang.pack_forget()
        CadreLien.pack_forget()
        CadreMoteur.pack_forget()
        CadreMeteo.pack(side="right")
    def ParaLang():
        CadreMeteo.pack_forget()
        CadreAssistant.pack_forget()
        CadreLien.pack_forget()
        CadreMoteur.pack_forget()
        CadreLang.pack(side="right")
    def ParaLien():
        CadreMeteo.pack_forget()
        CadreLang.pack_forget()
        CadreAssistant.pack_forget()
        CadreLien.pack_forget()
        CadreMoteur.pack_forget()
        CadreLien.pack(side="right")
    def ParaMoteur():
        CadreMeteo.pack_forget()
        CadreLang.pack_forget()
        CadreAssistant.pack_forget()
        CadreLien.pack_forget()
        CadreLien.pack_forget()
        CadreMoteur.pack(side="right")
    def FoncModif(file):
        Contenu = Lecture(file)
        ScreenModif = Toplevel()
        ScreenModif.maxsize(300,150)
        ScreenModif.minsize(300,150)
        ScreenModif.wait_visibility(ScreenModif)
        ScreenModif.wm_attributes('-alpha',0.9)
        ScreenModif.config(bg=SecondColor)
        LabelContenu = Label(ScreenModif,text=Contenu,font=("arial","20"),bg=SecondColor,fg=SecondTextColor)
        entry = Entry(ScreenModif)
        def Modif():
            Var = str(entry.get())
            Ecriture(file,Var)
            ScreenModif.destroy()
        Modif = Button(ScreenModif,text="Modifier",bg=SecondColor,fg=SecondTextColor,command=Modif).pack(side="right",anchor="s")
        LabelContenu.pack()
        entry.pack(side="left",anchor="s")
    def FoncModifSite(file,file2):
        Contenu = Lecture(file2)
        ScreenModif = Toplevel()
        ScreenModif.maxsize(400,250)
        ScreenModif.minsize(400,250)
        ScreenModif.wait_visibility(ScreenModif)
        ScreenModif.wm_attributes('-alpha',0.9)
        ScreenModif.config(bg=SecondColor)
        LabelContenu = Label(ScreenModif,text="Nom du site: "+Contenu,font=("arial","20"),bg=SecondColor,fg=SecondTextColor)
        frameName = Frame(ScreenModif,width=350,height=100,bg=SecondColor)
        labelName = Label(frameName,text="Nom :",bg=SecondColor,fg=SecondTextColor)
        entryName = Entry(frameName,width=30)
        labelLien = Label(frameName,text="Lien :",bg=SecondColor,fg=SecondTextColor)
        entryLien = Entry(frameName,width=30)
        def Modif():
            Var1 = str(entryName.get())
            Var2 = str(entryLien.get())
            Ecriture(file,Var2)
            Ecriture(file2,Var1)
            ScreenModif.destroy()
        Modif = Button(ScreenModif,text="Modifier",bg=SecondColor,fg=SecondTextColor,command=Modif).pack(side="bottom")
        LabelContenu.pack()
        frameName.place(relx=.5,rely=.5,anchor ="center")
        labelName.place(x="5",y="5")
        entryName.place(x="65",y="5")
        labelLien.place(x="5",y="65")
        entryLien.place(x="65",y="65")
    def ModifUser():
        FoncModif("Config/User.txt")
    def ModifNom():
        FoncModif("Config/Nom.txt")
    def MeteoChange1():
        FoncModif("Config/Ville.txt")
    def LangChange0():
        FoncModif("Config/Lang0.txt")
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
        FoncModifSite("Config/site/LienSite1.txt","Config/site/NomSite1.txt")
    def LienChange5():
        FoncModifSite("Config/site/LienSite2.txt","Config/site/NomSite2.txt")
    def LienChange6():
        FoncModifSite("Config/site/LienSite3.txt","Config/site/NomSite3.txt")
    def MoteurChange():
        file = "Config/moteur.txt"
        moteur = str(Lecture(file))
        ScreenModifM = Toplevel()
        ScreenModifM.maxsize(300,150)
        ScreenModifM.minsize(300,150)
        NewMoteur = StringVar(ScreenModifM)
        if moteur == "google":
            NewMoteur.set(listMoteur[0])
        if moteur == "duckduckgo":
            NewMoteur.set(listMoteur[1])
        if moteur == "ecosia":
            NewMoteur.set(listMoteur[2])
        if moteur == "qwant":
            NewMoteur.set(listMoteur[3])
        if moteur == "bing":
            NewMoteur.set(listMoteur[4])
        ScreenModifM.wait_visibility(ScreenModifM)
        ScreenModifM.wm_attributes('-alpha',0.9)
        ScreenModifM.config(bg=SecondColor)
        LabelInfo = Label(ScreenModifM,text="Moteur de recherche\n par défault",font=("arial","20"),bg=SecondColor,fg=SecondTextColor).pack()
        Moteur = OptionMenu(ScreenModifM,NewMoteur, *listMoteur)
        def Modif():
            VarMoteur = NewMoteur.get()
            Ecriture(file,VarMoteur)
            ScreenModifM.destroy()
        BoutonValider = Button(ScreenModifM,text="Valider",command=Modif,bg=SecondColor,fg=SecondTextColor)
        BoutonValider.pack(side="right")
        Moteur.pack(side="left")
    ScreenPara.title("Ryley : Paramétre")
    ScreenPara.maxsize(500,500)
    ScreenPara.minsize(500,500)
    ScreenPara.iconphoto(False,PhotoImage(file="image/Ryley.png"))
    ScreenPara.config(bg=SecondColor)
    LabelIndication = Label(ScreenPara,text="Paramétre",font=("arial","30"),bg=SecondColor,fg=SecondTextColor)
    #Cadre Para
    CadrePara = Frame(ScreenPara,bg="black",width=100,height=450)
    BoutonPara1 = Button(CadrePara,text="Assistant",bg=SecondColor,fg=SecondTextColor,command=ParaAssistant)
    BoutonPara2= Button(CadrePara,text="Méteo",bg=SecondColor,fg=SecondTextColor,command=ParaMeteo)
    BoutonPara3= Button(CadrePara,text="Traduction",bg=SecondColor,fg=SecondTextColor,command=ParaLang)
    BoutonPara4 = Button(CadrePara,text="Lien",bg=SecondColor,fg=SecondTextColor,command = ParaLien)
    #Cadre Assistant
    CadreAssistant = Frame(ScreenPara,bg=SecondColor,width=350,height=400)
    BoutonAssistant1 = Button(CadreAssistant,text="Change",bg=SecondColor,fg=SecondTextColor,font=("arial","15"),command=ModifNom)
    BoutonAssistant2 = Button(CadreAssistant,text="Change",bg=SecondColor,fg=SecondTextColor,font=("arial","15"),command=ModifUser)
    Assistant1 = Label(CadreAssistant,text="Nom de l'assistant",bg=SecondColor,fg=SecondTextColor,font=("arial","17"))
    Assistant2 = Label(CadreAssistant,text="Utilisateur",bg=SecondColor,fg=SecondTextColor,font=("arial","17"))
    #Cadre Meteo
    CadreMeteo = Frame(ScreenPara,bg=SecondColor,width=350,height=400)
    Meteo1 = Label(CadreMeteo,text="Lieu météo",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    BoutonMeteo1 = Button(CadreMeteo,text="Change",bg=SecondColor,fg=SecondTextColor,command=MeteoChange1,font=("arial","15"))
    #Cadre Lang
    CadreLang = Frame(ScreenPara,bg=SecondColor,width=350,height=400)
    Lang0 = Label(CadreLang,text="Langue par default",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    Lang1 = Label(CadreLang,text="Premier Langue",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    Lang2 = Label(CadreLang,text="Deuxiéme Langue",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    BoutonLang0 = Button(CadreLang,text="Change",bg=SecondColor,fg=SecondTextColor,command=LangChange0,font=("arial","15"))
    BoutonLang1 = Button(CadreLang,text="Change",bg=SecondColor,fg=SecondTextColor,command=LangChange1,font=("arial","15"))
    BoutonLang2 = Button(CadreLang,text="Change",bg=SecondColor,fg=SecondTextColor,command=LangChange2,font=("arial","15"))
    #Cadre Moteur
    CadreMoteur = Frame(ScreenPara,bg=SecondColor,width=350,height=400)
    Moteur1 = Label(CadreMoteur,text="Moteur",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    BoutonMoteur1 = Button(CadreMoteur,text="Change",bg=SecondColor,fg=SecondTextColor,command=MoteurChange,font=("arial","15"))
    #Cadre Lien
    CadreLien = Frame(ScreenPara,bg=SecondColor,width=350,height=400)
    Lien1  = Label(CadreLien,text="Google Drive",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    Lien2  = Label(CadreLien,text="Emplois du Temps",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    Lien3  = Label(CadreLien,text="Lien Angenda",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    Lien4  = Label(CadreLien,text="Site internet 1",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    Lien5  = Label(CadreLien,text="Site internet 2",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    Lien6  = Label(CadreLien,text="Site internet 3",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    BoutonLien1 = Button(CadreLien,text="Change",bg=SecondColor,fg=SecondTextColor,command=LienChange1,font=("arial","15"))
    BoutonLien2 = Button(CadreLien,text="Change",bg=SecondColor,fg=SecondTextColor,command=LienChange2,font=("arial","15"))
    BoutonLien3 = Button(CadreLien,text="Change",bg=SecondColor,fg=SecondTextColor,command=LienChange3,font=("arial","15"))
    BoutonLien4 = Button(CadreLien,text="Change",bg=SecondColor,fg=SecondTextColor,command=LienChange4,font=("arial","15"))
    BoutonLien5 = Button(CadreLien,text="Change",bg=SecondColor,fg=SecondTextColor,command=LienChange5,font=("arial","15"))
    BoutonLien6 = Button(CadreLien,text="Change",bg=SecondColor,fg=SecondTextColor,command=LienChange6,font=("arial","15"))
    BoutonPara5 = Button(CadrePara,text="Moteur\nRecherche",command=ParaMoteur,bg=SecondColor,fg=SecondTextColor)
    #Affichage
    LabelIndication.pack()
    CadrePara.pack(side="left")
    #Cadre Para
    BoutonPara1.place(x="5",y="5")
    BoutonPara2.place(x="10",y="85")
    BoutonPara3.place(x="2",y="165")
    BoutonPara4.place(x="10",y="245")
    BoutonPara5.place(x="2",y="325")
    #Cadre Assistant
    Assistant1.place(x="5",y="5")
    BoutonAssistant1.place(x="250",y="5")
    Assistant2.place(x="5",y="55")
    BoutonAssistant2.place(x="250",y="55")
    #Cadre Meteo
    Meteo1.place(x="5",y="5")
    BoutonMeteo1.place(x="250",y="5")
    #Cadre Lang
    Lang0.place(x="5",y="5")
    BoutonLang0.place(x="250",y="5")
    Lang1.place(x="5",y="55")
    BoutonLang1.place(x="250",y="55")
    Lang2.place(x="5",y="105")
    BoutonLang2.place(x="250",y="105")
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
    #Cadre Moteur
    Moteur1.place(x="5",y="5")
    BoutonMoteur1.place(x="250",y="5")
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
def Traduction():
    langue0=str(Lecture("Config/Lang0.txt"))
    langue1=str(Lecture("Config/Lang1.txt"))
    langue2=str(Lecture("Config/Lang2.txt"))
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
#Menu
RyleyMenu = Menu(screen,bg="white",fg="black")
FichierMenu = Menu(RyleyMenu,tearoff=0)
FichierMenu.add_command(label="Paramétre",command=Parametre)
FichierMenu.add_command(label="Test Internet",command=TestInternet)
RyleyMenu.add_cascade(label="Fichier",menu=FichierMenu)
RyleyMenu.add_command(label="A propos",command=APropos)
screen.config(menu=RyleyMenu)
#Code principal
Introduction()
BarreR = Entry(bottom,width=50)
def Interaction():
    requete=str(BarreR.get())
    NomAssistant = str(Lecture("Config/Nom.txt"))
    User = str(Lecture("Config/User.txt"))
    gDrive = str(Lecture("Config/GDrive.txt"))
    lienEDT = str(Lecture("Config/EDT.txt"))
    lienAgenda = str(Lecture("Config/Agenda.txt"))
    Moteur = str(Lecture("Config/moteur.txt"))
    LienSite1 = str(Lecture("Config/site/LienSite1.txt"))
    NameSite1 = str(Lecture("Config/site/NomSite1.txt"))
    LienSite2 = str(Lecture("Config/site/LienSite2.txt"))
    NameSite2 = str(Lecture("Config/site/NomSite2.txt"))
    LienSite3 = str(Lecture("Config/site/LienSite3.txt"))
    NameSite3 = str(Lecture("Config/site/NomSite3.txt"))
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
BoutonEnvoyer=Button(bottom,text="Envoyer",command=Interaction,bg=SecondColor,fg=SecondTextColor)
#Affichage
labelSpeak.place(x="10",y="300")
BarreR.place(x="0",y="130")
BoutonEnvoyer.place(x="415",y="125")
#Fin de la boucle
screen.mainloop()