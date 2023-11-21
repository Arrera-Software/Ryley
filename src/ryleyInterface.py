from tkinter import*
from src.gestionRyley import*
from librairy.travailJSON import*
from objet.codeHelp.codeHelp import*
from setting.arreraAssistantSetting import*
import time as t
from  ObjetsNetwork.arreraNeuron import*

class interfaceRyley:
    def __init__(self,gestionnaire:gestionRL,networkNeuron:ArreraNetwork):
        self.__gestionnaire = gestionnaire
        self.__arreraNetwork = networkNeuron
        self.__objetSetting = ArreraSettingAssistant("fichierJSON/configSetting.json","fichierJSON/configNeuron.json","fichierJSON/ryleyConfig.json","fichierJSON/configUser.json")
        self.__objetNetwork = network()
        self.__gestionnaire.setTheme()
        self.__mainColor = self.__gestionnaire.getMaincolor()
        self.__secondColor = self.__gestionnaire.getSecondColor()
        self.__mainTextColor = self.__gestionnaire.getMainTextcolor()
        self.__secondTextColor = self.__gestionnaire.getSecondTextColor()
        self.__BGTop = self.__gestionnaire.getBGTop()
        self.__BGBottom = self.__gestionnaire.getBGBottom()

    def windows(self):
        #Definition fenetre Tkinter
        self.__screen = Tk()
        #objet
        self.objetCodeHelp = CCodeHelp(self.__screen,self.__gestionnaire)
        #var
        self.bgTOP = PhotoImage(file = self.__BGTop)
        self.bgBOTTOM = PhotoImage(file = self.__BGBottom)
        self.iconWindows = PhotoImage(file="asset/Ryley.png")
        #Parametre Interface
        self.__screen.title("Ryley")
        self.__screen.config(bg=self.__mainColor)
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__screen.iconphoto(False,self.iconWindows)
        #Canvas
        self.__top = Canvas( self.__screen, width = 500,height = 400,bg=self.__mainColor, highlightthickness=0)
        self.__top.create_image( 0, 0, image = self.bgTOP, anchor = "nw")
        self.__bottom = Canvas( self.__screen, width = 500,height = 200,bg=self.__secondColor, highlightthickness=0)
        self.__bottom.create_image( 0, 0, image = self.bgBOTTOM, anchor = "nw")
        #Label
        self.__labelParole = Label(self.__top,text="Ryley "+": "+self.__arreraNetwork.boot(),bg=self.__mainColor,fg=self.__mainTextColor,font=("arial","14"), anchor="w")
        #Menu
        #Creation menu principale
        ryleyMenu = Menu(self.__screen,bg="white",fg="black")
        #Creation menu secondaire
        self.fichierMenu = Menu(ryleyMenu,tearoff=0)
        helpMenu = Menu(ryleyMenu,tearoff=0)
        #Ajout des command au menu fichierMenu
        self.fichierMenu.add_command(label="Paramétre",command=self.__activePara)
        self.fichierMenu.add_command(label="Test de connexion",command=self.__windowsEtatNetwork)
        self.fichierMenu.add_command(label="Calculatrice",command=self.__ouvertureCalculatrice)
        self.fichierMenu.add_command(label="Codehelp",command=self.__viewCodeHelp)
        #Ajout des command au menu helpMenu
        helpMenu.add_command(label="Documentation")
        helpMenu.add_command(label="A propos")
        #Ajout au menu principale tout les menu deroulant      
        ryleyMenu.add_cascade(label="Fichier",menu=self.fichierMenu)
        ryleyMenu.add_cascade(label="Aide",menu=helpMenu)
        self.__screen.configure(menu=ryleyMenu)
        #parametrage parametre
        self.__objetSetting.passageFonctionQuitter(self.__desactiverPara)
        #bouton
        boutonEnvoyer=Button(self.__bottom,text="Envoyer",bg=self.__secondColor,fg=self.__secondTextColor,font=("arial","15"),command=self.__envoi)
        #Afichage
        self.__barreR = Entry(self.__bottom,width=35,font=("arial","15"),relief=SOLID)
        self.__labelParole.place(x="10",y="300")
        self.__barreR.place(x="5",y="70")
        boutonEnvoyer.place(x="400",y="65")

    def bootCodehelp(self):
        self.fichierMenu.entryconfigure("Codehelp",label="Ryley",command=self.__unViewCodehelp)
        self.objetCodeHelp.view()
    
    def bootRyley(self):
        self.__top.place(x=0,y=0)
        self.__bottom.place(x=0,y=400)
        self.__detectionTouche(self.__screen,self.__envoi,13)
    
    def __viewCodeHelp(self):
        self.__top.place_forget()
        self.__bottom.place_forget()
        self.bootCodehelp()
    
    def __unViewCodehelp(self):
        self.fichierMenu.entryconfigure("Ryley",label="Codehelp",command=self.__viewCodeHelp)
        self.bootRyley()

    def __activePara(self):
        self.__top.place_forget()
        self.__bottom.place_forget()
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.fichierMenu.entryconfigure("Paramétre",label="Acceuil",command=self.__objetSetting.quittePara)
        self.__screen.update()
        self.__objetSetting.windows(self.__screen)
    
    def __desactiverPara(self):
        self.__top.place(x=0,y=0)
        self.__bottom.place(x=0,y=400)
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.fichierMenu.entryconfigure("Acceuil",label="Paramétre",command=self.__activePara)
        self.__screen.update()

    def __windowsEtatNetwork(self):
        wNetwork = Toplevel()
        wNetwork.title("Ryley : Reseau")
        wNetwork.iconphoto(False,self.iconWindows)
        wNetwork.maxsize(450,100)
        wNetwork.minsize(450,100)
        wNetwork.configure(bg=self.__mainColor)
        labelReseau = Label(wNetwork,fg=self.__mainTextColor,bg=self.__mainColor,font=("arial","15"))
        if self.__objetNetwork.getEtatInternet() == True :
            labelReseau.configure(text="Connecter a internet")
        else :
            labelReseau.configure(text="Non connecter a internet")
        labelReseau.place(relx=0.5,rely=0.5,anchor="center")

    def enableWindows(self):
        self.__screen.mainloop()

    def __detectionTouche(self,fenetre,fonc,touche):
        def anychar(event):
            if event.keycode == touche:
                fonc()               
        fenetre.bind("<Key>", anychar)

    def __envoi(self):
        statement = self.__barreR.get()
        self.__barreR.delete("0",END)
        var,texte = self.__arreraNetwork.neuron(statement)
        finalTexte = self.__formatageText(texte)
        if var == 15 :
            self.__labelParole.configure(text="Ryley "+":"+finalTexte, anchor="w")
            self.__screen.update()
            t.sleep(1.5)
            self.__screen.destroy()
        self.__labelParole.configure(text="Ryley "+":"+finalTexte, anchor="w")

    def __ouvertureCalculatrice(self):
        var,texte = self.__arreraNetwork.neuron("calculatrice")
        finalTexte = self.__formatageText(texte)
        self.__labelParole.configure(text="Ryley "+":"+finalTexte, anchor="w")
    
    def __formatageText(self,texte):
        if int(len(texte)) > 6 :
            texte1,texte2 = self.__division(texte,6)
            allTexte = texte1+"\n"+texte2
            if int(len(texte2)) > 6 :
                texte2,texte3 = self.__division(texte2,6)
                allTexte = texte1+"\n"+texte2+"\n"+texte3
                if int(len(texte3)) > 6 :
                    texte3,texte4 = self.__division(texte3,6)
                    allTexte = texte1+"\n"+texte2+"\n"+texte3+"\n"+texte4
        else :
            allTexte = texte
        return str(allTexte)

    def __division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)