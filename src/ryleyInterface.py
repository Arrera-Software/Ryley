from tkinter import*
from src.gestionRyley import*
from librairy.travailJSON import*
from setting.arreraAssistantSetting import*
import time as t
from  ObjetsNetwork.arreraNeuron import*

class interfaceRyley:
    def __init__(self,gestionnaire:gestionRL,networkNeuron:ArreraNetwork):
        self.gestionnaire = gestionnaire
        self.arreraNetwork = networkNeuron
        self.objetSetting = ArreraSettingAssistant("fichierJSON/configSetting.json","fichierJSON/configNeuron.json","fichierJSON/ryleyConfig.json","fichierJSON/configUser.json")
        self.objetNetwork = network()
        self.gestionnaire.setTheme()
        self.mainColor = self.gestionnaire.getMaincolor()
        self.secondColor = self.gestionnaire.getSecondColor()
        self.mainTextColor = self.gestionnaire.getMainTextcolor()
        self.secondTextColor = self.gestionnaire.getSecondTextColor()
        self.BGTop = self.gestionnaire.getBGTop()
        self.BGBottom = self.gestionnaire.getBGBottom()

    def fenetreRyley(self):
        #Definition fenetre Tkinter
        self.screen = Tk()
        #var
        self.bgTOP = PhotoImage(file = self.BGTop)
        self.bgBOTTOM = PhotoImage(file = self.BGBottom)
        self.iconWindows = PhotoImage(file="asset/Ryley.png")
        #Parametre Interface
        self.screen.title("Ryley")
        self.screen.config(bg=self.mainColor)
        self.screen.maxsize(500,600)
        self.screen.minsize(500,600)
        self.screen.iconphoto(False,self.iconWindows)
        #Canvas
        self.top = Canvas( self.screen, width = 500,height = 400,bg=self.mainColor, highlightthickness=0)
        self.top.create_image( 0, 0, image = self.bgTOP, anchor = "nw")
        self.bottom = Canvas( self.screen, width = 500,height = 200,bg=self.secondColor, highlightthickness=0)
        self.bottom.create_image( 0, 0, image = self.bgBOTTOM, anchor = "nw")
        #Label
        self.labelParole = Label(self.top,text="Ryley "+": "+self.arreraNetwork.boot(),bg=self.mainColor,fg=self.mainTextColor,font=("arial","14"), anchor="w")
        #Menu
        #Creation menu principale
        ryleyMenu = Menu(self.screen,bg="white",fg="black")
        #Creation menu secondaire
        self.fichierMenu = Menu(ryleyMenu,tearoff=0)
        helpMenu = Menu(ryleyMenu,tearoff=0)
        #Ajout des command au menu fichierMenu
        self.fichierMenu.add_command(label="Paramétre",command=self.activePara)
        self.fichierMenu.add_command(label="Test de connexion",command=self.windowsEtatNetwork)
        self.fichierMenu.add_command(label="Calculatrice",command=self.ouvertureCalculatrice)
        self.fichierMenu.add_command(label="Codehelp")
        #Ajout des command au menu helpMenu
        helpMenu.add_command(label="Documentation")
        helpMenu.add_command(label="A propos")
        #Ajout au menu principale tout les menu deroulant      
        ryleyMenu.add_cascade(label="Fichier",menu=self.fichierMenu)
        ryleyMenu.add_cascade(label="Aide",menu=helpMenu)
        self.screen.configure(menu=ryleyMenu)
        #parametrage parametre
        self.objetSetting.passageFonctionQuitter(self.desactiverPara)
        #bouton
        boutonEnvoyer=Button(self.bottom,text="Envoyer",bg=self.secondColor,fg=self.secondTextColor,font=("arial","15"),command=self.envoi)
        #Afichage
        self.top.place(x=0,y=0)
        self.bottom.place(x=0,y=400)
        self.barreR = Entry(self.bottom,width=35,font=("arial","15"),relief=SOLID)
        self.labelParole.place(x="10",y="300")
        self.barreR.place(x="5",y="70")
        boutonEnvoyer.place(x="400",y="65")
        self._detectionTouche(self.screen,self.envoi,13)

    def activePara(self):
        self.top.place_forget()
        self.bottom.place_forget()
        self.screen.maxsize(500,600)
        self.screen.minsize(500,600)
        self.fichierMenu.entryconfigure("Paramétre",label="Ryley",command=self.objetSetting.quittePara)
        self.screen.update()
        self.objetSetting.windows(self.screen)
    
    def desactiverPara(self):
        self.top.place(x=0,y=0)
        self.bottom.place(x=0,y=400)
        self.screen.maxsize(500,600)
        self.screen.minsize(500,600)
        self.fichierMenu.entryconfigure("Ryley",label="Paramétre",command=self.activePara)
        self.screen.update()

    def windowsEtatNetwork(self):
        wNetwork = Toplevel()
        wNetwork.title("Ryley : Reseau")
        wNetwork.iconphoto(False,self.iconWindows)
        wNetwork.maxsize(450,100)
        wNetwork.minsize(450,100)
        wNetwork.configure(bg=self.mainColor)
        labelReseau = Label(wNetwork,fg=self.mainTextColor,bg=self.mainColor,font=("arial","15"))
        if self.objetNetwork.getEtatInternet() == True :
            labelReseau.configure(text="Connecter a internet")
        else :
            labelReseau.configure(text="Non connecter a internet")
        labelReseau.place(relx=0.5,rely=0.5,anchor="center")

    def activeRyley(self):
        self.screen.mainloop()

    def _detectionTouche(self,fenetre,fonc,touche):
        def anychar(event):
            if event.keycode == touche:
                fonc()               
        fenetre.bind("<Key>", anychar)

    def envoi(self):
        statement = self.barreR.get()
        self.barreR.delete("0",END)
        var,texte = self.arreraNetwork.neuron(statement)
        finalTexte = self._formatageText(texte)
        if var == 15 :
            self.labelParole.configure(text="Ryley "+":"+finalTexte, anchor="w")
            self.screen.update()
            t.sleep(1.5)
            self.screen.destroy()
        self.labelParole.configure(text="Ryley "+":"+finalTexte, anchor="w")

    def ouvertureCalculatrice(self):
        var,texte = self.arreraNetwork.neuron("calculatrice")
        finalTexte = self._formatageText(texte)
        self.labelParole.configure(text="Ryley "+":"+finalTexte, anchor="w")
    
    def _formatageText(self,texte):
        if int(len(texte)) > 6 :
            texte1,texte2 = self._division(texte,6)
            allTexte = texte1+"\n"+texte2
            if int(len(texte2)) > 6 :
                texte2,texte3 = self._division(texte2,6)
                allTexte = texte1+"\n"+texte2+"\n"+texte3
                if int(len(texte3)) > 6 :
                    texte3,texte4 = self._division(texte3,6)
                    allTexte = texte1+"\n"+texte2+"\n"+texte3+"\n"+texte4
        else :
            allTexte = texte
        return str(allTexte)

    def _division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)