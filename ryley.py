from function.JSON import*
from setting.setting import*
from function.internet import*
from function.traduction import*
from API.API import*
from src.varriable import*
from neuronRyley.neuronMain import*
from neuronRyley.neuronSearch import*
from neuronRyley.neuronTime import*
from neuronRyley.neuroneCodeHelp import*
from tkinter import*

from src.ryleySRC import*

import random
import datetime
class Ryley :
    def __init__(self):
        self.nameAssistant = lectureJSON("setting/config.json","nomAssistant")
        self.user = lectureJSON("setting/config.json","user")
        #Definition fenetre Tkinter
        self.screen = Tk()
        #var
        self.bgTOP = PhotoImage(file = "image/BGTop.png")
        self.bgBOTTOM = PhotoImage(file = "image/BGBottom.png")
        self.imgMicro = PhotoImage(file="image/imgMicro.png")
        self.listLanguage = ["all","python","javascript","html","cpp","c","css","php","openjdk"]
        self.varLanguage = StringVar(self.screen)
        self.screen.title("Ryley")
        self.screen.config(bg=mainColor)
        self.screen.maxsize(500,600)
        self.screen.minsize(500,600)
        self.screen.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        self.top = Canvas( self.screen, width = 500,height = 400)
        self.top.pack()
        self.top.create_image( 0, 0, image = self.bgTOP, anchor = "nw")
        self.bottom = Canvas( self.screen, width = 500,height = 200)
        self.bottom.pack(side="bottom")
        self.bottom.create_image( 0, 0, image = self.bgBOTTOM, anchor = "nw")
        #Label
        self.labelParole = Label(self.top,text=self.nameAssistant+":",bg=mainColor,fg=mainTextColor,font=("arial","14"))
        self.labelIndication = Label(self.bottom,bg=secondColor,fg=secondTextColor,font=("arial","14"))
        #Menu
        self.ryleyMenu = Menu(self.screen,bg="white",fg="black")
        self.fichierMenu = Menu(self.ryleyMenu,tearoff=0)
        self.appMenu = Menu(self.ryleyMenu,tearoff=0)
        self.fichierMenu.add_command(label="Paramétre",command=Setting)
        self.fichierMenu.add_command(label="Test Internet",command=TestInternet)
        self.appMenu.add_command(label="Calculatrice",command=Calcule)
        self.ryleyMenu.add_cascade(label="Fichier",menu=self.fichierMenu)
        self.ryleyMenu.add_cascade(label="Fonction",menu=self.appMenu)
        self.ryleyMenu.add_command(label="A propos",command=self.APropos)
        self.screen.config(menu=self.ryleyMenu)
        #bouton
        self.boutonEnvoyer=Button(self.bottom,text="Envoyer",command=self.envoi,bg=secondColor,fg=secondTextColor,font=("arial","15"))
        self.boutonMicro = Button(self.bottom,image=self.imgMicro,command=self.micro)
        #option menu
        self.choixLanguage = OptionMenu(self.bottom,self.varLanguage,*self.listLanguage)
        #Code principal
        self.Introduction()
        self.barreR = Entry(self.bottom,width=35,font=("arial","15"),relief=SOLID)
        self.labelParole.place(x="10",y="300")
        self.barreR.place(x="5",y="70")
        self.boutonEnvoyer.place(x="400",y="65")
        self.boutonMicro.place(x="25",y="115")
        #Fin de la boucle
        self.screen.mainloop()
    
    def APropos(self):
        self.screenAPropos = Toplevel()
        self.screenAPropos.title("Ryley")
        self.screenAPropos.maxsize(425,170)
        self.screenAPropos.minsize(425,170)
        self.screenAPropos.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        self.screenAPropos.config(bg=mainColor)
        Label(self.screenAPropos,text="Assistant Personnelle Ryley\nCréer par:\nSpeedyCreator\net\nWiruto2",font=("arial","20"),bg=mainColor,fg=mainTextColor).pack()       

    def Introduction(self):
        hour=datetime.datetime.now().hour
        if hour >= 0 and hour <=5:
            RyleySRC.speak("Zzzz "+self.user+" Il faut peut etre dormir non?",self.labelParole,self.nameAssistant)
        else :
            if hour >= 6 and hour <= 9 :
                RyleySRC.speak("Hey "+self.user+" as-tu bien dormi?",self.labelParole,self.nameAssistant)
            else :
                if hour >= 10 and hour <= 12:
                    RyleySRC.speak("Salut "+self.user+" comment ce passe ta matinée?",self.labelParole,self.nameAssistant)
                else :
                    if hour >= 13 and hour <= 17:
                        RyleySRC.speak("Alors "+self.user+" pret a travailler?",self.labelParole,self.nameAssistant)
                    else :
                        if hour >= 18 and hour <= 21 :
                            RyleySRC.speak("Alors "+self.user+" que veut-tu faire ce soir ?",self.labelParole,self.nameAssistant)
                        else :
                            if hour >= 22 and hour <= 23:
                                RyleySRC.speak("*baille* "+self.user+" ? Que fais tu si tard?",self.labelParole,self.nameAssistant)
                            else :
                                RyleySRC.speak("Salut "+self.user,self.labelParole,self.nameAssistant)
    
    
    def phraseAttent(self):
        nbrad = random.randrange(1,6)
        if nbrad == 1 :
            RyleySRC.speak("En quoi je peux d'aider "+self.user,self.labelParole,self.nameAssistant)
        else :
            if nbrad == 2 :
                RyleySRC.speak("J'espére que j'ai pu d'aider "+self.user,self.labelParole,self.nameAssistant)
            else :
                if nbrad == 3 :
                    RyleySRC.speak("En quoi je peux encore d'aider "+self.user,self.labelParole,self.nameAssistant) 
                else :
                    if nbrad == 4 :
                        RyleySRC.speak("Je peux encore plus d'aider "+self.user,self.labelParole,self.nameAssistant)
                    else :
                        if nbrad == 5 :
                            RyleySRC.speak("Dit-moi si je peux d'aider "+self.user,self.labelParole,self.nameAssistant)
                        else :
                            RyleySRC.speak("J'espere que mon uttilisation te sois utile "+self.user,self.labelParole,self.nameAssistant)
    
    def micro(self):
        RyleySRC.takeCommand(self.barreR)
    
    def envoi(self):
        requete=str(self.barreR.get())
        self.barreR.delete(0,END)
        varRyley = Main(requete,self.screen,self.user,self.labelParole,self.nameAssistant)
        if varRyley == 1 :
            self.phraseAttent()
        else :
            varRyley = search(requete,self.screen,self.user,self.labelParole,self.nameAssistant)
            if varRyley == 1 :
                self.phraseAttent()
            else :
                varRyley = Time(requete,self.screen,self.user,self.labelParole,self.nameAssistant)
                if varRyley == 1 :
                    self.phraseAttent()
                else :
                    varRyley = neuronCodeHelp(requete,self.screen,self.user,self.labelParole,self.nameAssistant,self.barreR,self.top,self.boutonEnvoyer,self.choixLanguage,self.varLanguage,self.envoi,self.top,self.labelIndication)
                    if varRyley == 1 :
                        self.phraseAttent()
                    else :
                        if (varRyley != 2):
                            RyleySRC.speak("Je peux pas répondre a ta requette "+self.user,self.labelParole,self.nameAssistant)
    