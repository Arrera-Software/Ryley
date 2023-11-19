from tkinter import*
from src.gestionRyley import*
from librairy.travailJSON import*
from setting.arreraAssistantSetting import*
import time as t
from PIL import Image, ImageTk
from  ObjetsNetwork.arreraNeuron import*

class interfaceRyley:
    def __init__(self,gestionnaire:gestionRL,networkNeuron:ArreraNetwork):
        self.gestionnaire = gestionnaire
        self.arreraNetwork = networkNeuron
        self.objetSetting = ArreraSettingAssistant("fichierJSON/configSetting.json","fichierJSON/configNeuron.json","fichierJSON/ryleyConfig.json","fichierJSON/configUser.json")
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
        #self.imgMicro = PhotoImage(file="image/imgMicro.png")
        self.listLanguage = ["all","python","javascript","html","cpp","c","css","php","openjdk","microsoft"]
        self.varLanguage = StringVar(self.screen)
        #Parametre Interface
        self.screen.title("Ryley")
        self.screen.config(bg=self.mainColor)
        self.screen.maxsize(500,600)
        self.screen.minsize(500,600)
        self.screen.iconphoto(False,PhotoImage(file="asset/Ryley.png"))
        #Canvas
        self.top = Canvas( self.screen, width = 500,height = 400,bg=self.mainColor, highlightthickness=0)
        self.top.create_image( 0, 0, image = self.bgTOP, anchor = "nw")
        self.bottom = Canvas( self.screen, width = 500,height = 200,bg=self.secondColor, highlightthickness=0)
        self.bottom.create_image( 0, 0, image = self.bgBOTTOM, anchor = "nw")
        #Label
        self.labelParole = Label(self.top,text="Ryley "+": "+self.arreraNetwork.boot(),bg=self.mainColor,fg=self.mainTextColor,font=("arial","14"), anchor="w")
        labelIndication = Label(self.bottom,bg=self.secondColor,fg=self.secondTextColor,font=("arial","14"))
        #Menu
        #Creation menu principale
        ryleyMenu = Menu(self.screen,bg="white",fg="black")
        #Creation menu secondaire
        self.fichierMenu = Menu(ryleyMenu,tearoff=0)
        appMenu = Menu(ryleyMenu,tearoff=0)
        codeHelpMenu = Menu(appMenu,tearoff=0)
        helpMenu = Menu(appMenu,tearoff=0)
        
        #Ajout des command au menu fichierMenu
        self.fichierMenu.add_command(label="Paramétre",command=self.activePara)
        self.fichierMenu.add_command(label="Test de connexion")
        
        #Ajout des command au menu helpMenu
        helpMenu.add_command(label="Documentation")
        helpMenu.add_command(label="A propos")
        
        #Ajout des command au menu appMenu
        appMenu.add_command(label="Calculatrice")
        appMenu.add_cascade(label="codeHelp")
        
        #Ajout des command au menu codeHelpMenu
        """
        self.codeHelpMenu.add_command(label="Lancer CodeHelp",command=lambda : CodeHelp(self.top,self.barreR,self.labelParole,self.boutonEnvoyer,self.ryleyMenu,self.choixLanguage,self.nameAssistant,self.envoi,self.labelIndication,"1",self.ryleyMenu,self.screen))
        self.codeHelpMenu.add_command(label="Recherche de documentation",command=lambda : CodeHelp.rechercheDoc(self.top,self.barreR,self.labelParole,self.boutonEnvoyer,self.choixLanguage,self.varLanguage,self.nameAssistant,self.envoi))
        self.codeHelpMenu.add_command(label="Connextion a github",command=lambda : CodeHelp.PageGithub(self.top,self.barreR,self.labelParole,self.boutonEnvoyer,self.nameAssistant,self.envoi,self.labelIndication,))
        self.codeHelpMenu.add_command(label="Librairy",command=lambda : webbrowser.open("https://github.com/baptistepau/RyleyCodeHelpLibrairy"))
        self.codeHelpMenu.add_command(label="Editeur de Documentation",command=CodeHelp.EditeurDoc)
        self.codeHelpMenu.add_command(label="Selectionneur de couleur",command=CodeHelp.ColorSelector)
        self.codeHelpMenu.add_command(label="Organisateur de varriable",command=CodeHelp.orgranisateurVarriable)
        """
        
        
        #Ajout au menu principale tout les menu deroulant      
        ryleyMenu.add_cascade(label="Fichier",menu=self.fichierMenu)
        ryleyMenu.add_cascade(label="Fonction",menu=appMenu)
        ryleyMenu.add_cascade(label="Aide",menu=helpMenu)
        
        self.screen.configure(menu=ryleyMenu)
        #parametrage parametre
        self.objetSetting.passageFonctionQuitter(self.desactiverPara)
        #bouton
        boutonEnvoyer=Button(self.bottom,text="Envoyer",bg=self.secondColor,fg=self.secondTextColor,font=("arial","15"),command=self.envoi)
        #boutonMicro = Button(self.bottom,image=self.imgMicro,command=self.micro)
        #option menu
        choixLanguage = OptionMenu(self.bottom,self.varLanguage,*self.listLanguage)
        #Afichage
        self.top.place(x=0,y=0)
        self.bottom.place(x=0,y=400)

        self.barreR = Entry(self.bottom,width=35,font=("arial","15"),relief=SOLID)
        self.labelParole.place(x="10",y="300")
        self.barreR.place(x="5",y="70")
        boutonEnvoyer.place(x="400",y="65")
        self._detectionTouche(self.screen,self.envoi,13)
        #Fin de la boucle

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

    

    def activeRyley(self):
        self.screen.mainloop()

    def _detectionTouche(self,fenetre,fonc,touche):
        def anychar(event):
            if event.keycode == touche:
                fonc()               
        fenetre.bind("<Key>", anychar)

    def envoi(self):
        statement = self.barreR.get().lower
        self.barreR.delete("0",END)
        var,texte = self.arreraNetwork.neuron(statement)
        finalTexte = self._formatageText(texte)
        if var == 15 :
            self.labelParole.configure(text="Ryley "+":"+finalTexte, anchor="w")
            self.screen.update()
            t.sleep(1.5)
            self.screen.destroy()
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