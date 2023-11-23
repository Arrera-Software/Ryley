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
        self.__objetNetwork = network()
    
    def __setTheme(self):
        self.__gestionnaire.setTheme()
        self.__mainColor = self.__gestionnaire.getMaincolor()
        self.__secondColor = self.__gestionnaire.getSecondColor()
        self.__mainTextColor = self.__gestionnaire.getMainTextcolor()
        self.__secondTextColor = self.__gestionnaire.getSecondTextColor()
        self.__BGTop = self.__gestionnaire.getBGTop()
        self.__BGBottom = self.__gestionnaire.getBGBottom()
        self.__screen.config(bg=self.__mainColor)
        self.bgTOP = PhotoImage(file = self.__BGTop)
        self.bgBOTTOM = PhotoImage(file = self.__BGBottom)
        self.__boutonEnvoyer.configure(bg=self.__secondColor,fg=self.__secondTextColor)
        self.__top.configure(bg=self.__mainColor)
        self.__bottom.configure(bg=self.__secondColor)
        self.__top.create_image( 0, 0, image = self.bgTOP, anchor = "nw")
        self.__bottom.create_image( 0, 0, image = self.bgBOTTOM, anchor = "nw")
        self.__labelParole.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        self.__ryleyMenu.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        if self.__mainColor == "#ffffff" :
            self.__objetSetting = ArreraSettingAssistant("fichierJSON/configSettingLight.json","fichierJSON/configNeuron.json","fichierJSON/ryleyConfig.json","fichierJSON/configUser.json")
        else :
            if self.__mainColor == "#000000" :
                self.__objetSetting = ArreraSettingAssistant("fichierJSON/configSettingDark.json","fichierJSON/configNeuron.json","fichierJSON/ryleyConfig.json","fichierJSON/configUser.json")
            else :
                self.__objetSetting = ArreraSettingAssistant("fichierJSON/configSettingLight.json","fichierJSON/configNeuron.json","fichierJSON/ryleyConfig.json","fichierJSON/configUser.json")
        self.__objetSetting.passageFonctionQuitter(self.__desactiverPara)
    
    def windows(self):
        #Definition fenetre Tkinter
        self.__screen = Tk()
        self.__iconWindows = PhotoImage(file="asset/Ryley.png")
        #Parametre Interface
        self.__screen.title("Ryley")
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__screen.iconphoto(False,self.__iconWindows)
        #Canvas
        self.__top = Canvas( self.__screen, width = 500,height = 400, highlightthickness=0)
        self.__bottom = Canvas( self.__screen, width = 500,height = 200, highlightthickness=0)
        #Label
        self.__labelParole = Label(self.__top,text="Ryley "+": "+self.__arreraNetwork.boot(),font=("arial","14"), anchor="w")
        #Menu
        #Creation menu principale
        self.__ryleyMenu = Menu(self.__screen)
        #Creation menu secondaire
        self.__fichierMenu = Menu(self.__ryleyMenu,tearoff=0)
        helpMenu = Menu(self.__ryleyMenu,tearoff=0)
        #Ajout des command au menu fichierMenu
        self.__fichierMenu.add_command(label="Paramétre",command=self.__activePara)
        self.__fichierMenu.add_command(label="Test de connexion",command=self.__windowsEtatNetwork)
        self.__fichierMenu.add_command(label="Calculatrice",command=self.__ouvertureCalculatrice)
        self.__fichierMenu.add_command(label="Codehelp",command=self.__viewCodeHelp)
        #Ajout des command au menu helpMenu
        helpMenu.add_command(label="Documentation")
        helpMenu.add_command(label="A propos")
        #Ajout au menu principale tout les menu deroulant      
        self.__ryleyMenu.add_cascade(label="Fichier",menu=self.__fichierMenu)
        self.__ryleyMenu.add_cascade(label="Aide",menu=helpMenu)
        self.__screen.configure(menu=self.__ryleyMenu)
        #parametrage parametre
        self.__boutonEnvoyer=Button(self.__bottom,text="Envoyer",font=("arial","15"),command=self.__envoi)
        #Application du theme
        self.__setTheme()
        #objet codehelp
        self.objetCodeHelp = CCodeHelp(self.__screen,self.__gestionnaire)
        self.objetCodeHelp.setFonctionback(self.__unViewCodehelp)
        #Afichage
        self.__barreR = Entry(self.__bottom,width=35,font=("arial","15"),relief=SOLID)
        self.__labelParole.place(x="10",y="300")
        self.__barreR.place(x="5",y="70")
        self.__boutonEnvoyer.place(x="400",y="65")
    

    def bootCodehelp(self):
        self.__fichierMenu.entryconfigure("Codehelp",label="Ryley",command=self.__unViewCodehelp)
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
        self.__fichierMenu.entryconfigure("Ryley",label="Codehelp",command=self.__viewCodeHelp)
        self.objetCodeHelp.unView()
        self.bootRyley()
        self.__screen.title("Ryley")
        self.__screen.iconphoto(False,self.__iconWindows)
        self.__screen.update()

    def __activePara(self):
        #fichierConfigSetting = jsonWork("fichierJSON/configSetting.json")
        #fichierConfigSetting.EcritureJSON("color1",self.__mainColor)
        self.__top.place_forget()
        self.__bottom.place_forget()
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__fichierMenu.entryconfigure("Paramétre",label="Acceuil",command=self.__objetSetting.quittePara)
        self.__screen.update()
        self.__objetSetting.windows(self.__screen)
        self.__objetSetting.mainView() 
        self.__screen.mainloop()
        
    
    def __desactiverPara(self):
        #Application du theme
        self.__setTheme()
        self.__screen.update()
        self.__top.place(x=0,y=0)
        self.__bottom.place(x=0,y=400)
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__fichierMenu.entryconfigure("Acceuil",label="Paramétre",command=self.__activePara)
        self.__screen.update()
        self.__screen.title("Ryley")

    def __windowsEtatNetwork(self):
        wNetwork = Toplevel()
        wNetwork.title("Ryley : Reseau")
        wNetwork.iconphoto(False,self.__iconWindows)
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