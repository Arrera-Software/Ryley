#fichier
from function.JSON import*
from setting.setting import*
from function.internet import*
from function.traduction import*
from API.API import*
from src.systeme import*
from neuronRyley.neuronMain import*
from neuronRyley.neuronSearch import*
from neuronRyley.neuronTime import*
from neuronRyley.neuroneCodeHelp import*
from function.detectionTouche import *
#module
from tkinter import*
from PIL import Image, ImageTk
from src.ryleySRC import*
import random
import datetime
def openSoftware(name):
    name = str(name)
    subprocess.Popen(["cmd", "/c", "start", name])

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
        self.listLanguage = ["all","python","javascript","html","cpp","c","css","php","openjdk","microsoft"]
        self.varLanguage = StringVar(self.screen)
        #Parametre Interface
        self.screen.title("Ryley")
        self.screen.config(bg=mainColor)
        self.screen.maxsize(500,600)
        self.screen.minsize(500,600)
        self.screen.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        self.top = Canvas( self.screen, width = 500,height = 400,bg=mainColor)
        self.top.place(x=0,y=0)
        self.top.create_image( 0, 0, image = self.bgTOP, anchor = "nw")
        self.bottom = Canvas( self.screen, width = 500,height = 200,bg=secondColor)
        self.bottom.place(x=0,y=400)
        self.bottom.create_image( 0, 0, image = self.bgBOTTOM, anchor = "nw")
        #Label
        self.labelParole = Label(self.top,text=self.nameAssistant+":",bg=mainColor,fg=mainTextColor,font=("arial","14"))
        self.labelIndication = Label(self.bottom,bg=secondColor,fg=secondTextColor,font=("arial","14"))
        #objet 
        self.sourceRyley = RyleySRC(self.labelParole,self.nameAssistant)
        #Menu
        #Creation menu principale
        self.ryleyMenu = Menu(self.screen,bg="white",fg="black")
        #Creation menu secondaire
        self.fichierMenu = Menu(self.ryleyMenu,tearoff=0)
        self.appMenu = Menu(self.ryleyMenu,tearoff=0)
        self.codeHelpMenu = Menu(self.appMenu,tearoff=0)
        self.helpMenu = Menu(self.appMenu,tearoff=0)
        
        #Ajout des command au menu fichierMenu
        self.fichierMenu.add_command(label="Paramétre",command=Setting)
        self.fichierMenu.add_command(label="Test de connexion",command=self.InterfaceTestConnection)
        
        #Ajout des command au menu helpMenu
        self.helpMenu.add_command(label="Documentation",command=lambda : openSoftware("Documentation/RyleyDoc.pdf"))
        self.helpMenu.add_command(label="A propos",command=self.APropos)
        
        #Ajout des command au menu appMenu
        self.appMenu.add_command(label="Calculatrice",command=lambda : Calcule(mainColor,mainTextColor,"Ryley : Calculatrice"))
        self.appMenu.add_cascade(label="codeHelp",menu=self.codeHelpMenu)
        
        #Ajout des command au menu codeHelpMenu
        self.codeHelpMenu.add_command(label="Lancer CodeHelp",command=lambda : CodeHelp(self.top,self.barreR,self.labelParole,self.boutonEnvoyer,self.ryleyMenu,self.choixLanguage,self.nameAssistant,self.envoi,self.labelIndication,"1",self.ryleyMenu,self.screen))
        self.codeHelpMenu.add_command(label="Recherche de documentation",command=lambda : CodeHelp.rechercheDoc(self.top,self.barreR,self.labelParole,self.boutonEnvoyer,self.choixLanguage,self.varLanguage,self.nameAssistant,self.envoi))
        self.codeHelpMenu.add_command(label="Connextion a github",command=lambda : CodeHelp.PageGithub(self.top,self.barreR,self.labelParole,self.boutonEnvoyer,self.nameAssistant,self.envoi,self.labelIndication,))
        self.codeHelpMenu.add_command(label="Librairy",command=lambda : webbrowser.open("https://github.com/baptistepau/RyleyCodeHelpLibrairy"))
        self.codeHelpMenu.add_command(label="Editeur de Documentation",command=CodeHelp.EditeurDoc)
        self.codeHelpMenu.add_command(label="Selectionneur de couleur",command=CodeHelp.ColorSelector)
        self.codeHelpMenu.add_command(label="Organisateur de varriable",command=CodeHelp.orgranisateurVarriable)
        
        #Ajout au menu principale tout les menu deroulant      
        self.ryleyMenu.add_cascade(label="Fichier",menu=self.fichierMenu)
        self.ryleyMenu.add_cascade(label="Fonction",menu=self.appMenu)
        self.ryleyMenu.add_cascade(label="Aide",menu=self.helpMenu)
        
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
        #Prise en charge tout entrer
        Touche(self.screen,self.envoi,13)
        #Fin de la boucle
        self.screen.mainloop()
        
    
    def APropos(self):#Fonction qui correspond a la fentre apropos
        #Variable
        nameApp = "Ryley"#Definir le nom de l'app
        versionApp = "I2023-2.50.1"#Definir le nom de la version
        imagePath = "image/Ryley.png"#Indiquer l'emplacement de l'icon
        copyrightApp = "Copyright Arrera Software by Baptiste P and Wiruto2 2023-"
        tailleIMG = (100,100)
        #Creation de la fenetre
        about = Toplevel()
        about.config(bg="white")
        about.title("A propos :"+nameApp)
        about.maxsize(400,300)
        about.minsize(400,300)
        #Traitement Image
        imageOrigine = Image.open(imagePath)
        imageRedim = imageOrigine.resize(tailleIMG)
        icon = ImageTk.PhotoImage(imageRedim)
        #Label
        labelIcon = Label(about,image=icon,bg="white")
        labelName = Label(about,text="\n"+nameApp+"\n",font=("arial","12"),bg="white")
        labelVersion = Label(about,text=versionApp+"\n",font=("arial","11"),bg="white")
        labelCopyright = Label(about,text=copyrightApp,font=("arial","9"),bg="white")
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()
        about.mainloop() 
        
    def InterfaceTestConnection(self):
        screenInternet = Toplevel()
        network = internet
        screenInternet.title("Ryley")
        screenInternet.maxsize(425,70)
        screenInternet.minsize(425,70)
        screenInternet.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        screenInternet.config(bg=MainColor)
        labelInfo = Label(screenInternet,font=("arial","20"),bg=MainColor,fg=MainTextColor)
        testing = network.testInternet()
        if testing == True :
            labelInfo.config(text="Internet disponible")
        else :
            labelInfo.config(text="Internet non disponible")
        labelInfo.pack()
        
    def Introduction(self):#Fonction qui ce lance au demarage de l'assistant
        hour=datetime.datetime.now().hour
        if hour >= 0 and hour <=5:
            self.sourceRyley.speak("Zzzz "+self.user+" Il faut peut etre dormir non?",)
        else :
            if hour >= 6 and hour <= 9 :
                self.sourceRyley.speak("Hey "+self.user+" as-tu bien dormi?")
            else :
                if hour >= 10 and hour <= 12:
                    self.sourceRyley.speak("Salut "+self.user+" comment ce passe ta matinée?")
                else :
                    if hour >= 13 and hour <= 17:
                        self.sourceRyley.speak("Alors "+self.user+" pret a travailler?")
                    else :
                        if hour >= 18 and hour <= 21 :
                            self.sourceRyley.speak("Alors "+self.user+" que veut-tu faire ce soir ?")
                        else :
                            if hour >= 22 and hour <= 23:
                                self.sourceRyley.speak("*baille* "+self.user+" ? Que fais tu si tard?")
                            else :
                               self.sourceRyley.speak("Salut "+self.user)
    
    
    def phraseAttent(self):#Fonction qui permet a l'assistant de dire une phrase entre chaque demande de service
        nbrad = random.randrange(1,6)
        if nbrad == 1 :
            self.sourceRyley.speak("En quoi je peux d'aider "+self.user)
        else :
            if nbrad == 2 :
                self.sourceRyley.speak("J'espére que j'ai pu d'aider "+self.user)
            else :
                if nbrad == 3 :
                    self.sourceRyley.speak("En quoi je peux encore d'aider "+self.user) 
                else :
                    if nbrad == 4 :
                        self.sourceRyley.speak("Je peux encore plus d'aider "+self.user)
                    else :
                        if nbrad == 5 :
                            self.sourceRyley.speak("Dit-moi si je peux d'aider "+self.user)
                        else :
                            self.sourceRyley.speak("J'espere que mon uttilisation te sois utile "+self.user)
    
    def micro(self):#Fontion prise de command par la voix
        Micro(self.barreR).takeCommand()
    
    def envoi(self):#Fonction qui correspond a l'envoi des requette au neuron de traitement de l'assistant
        requete=str(self.barreR.get())
        self.barreR.delete(0,END)
        varRyley = Main(requete,self.screen,self.user,self.sourceRyley)
        if varRyley == 1 :
            self.phraseAttent()
        else :
            varRyley = Neuronsearch(requete,self.screen,self.user,self.sourceRyley)
            if varRyley == 1 :
                self.phraseAttent()
            else :
                varRyley = Time(requete,self.screen,self.user,self.sourceRyley)
                if varRyley == 1 :
                    self.phraseAttent()
                else :
                    varRyley = neuronCodeHelp(requete,self.screen,self.user,self.labelParole,self.nameAssistant,self.barreR,self.top,self.boutonEnvoyer,self.choixLanguage,self.varLanguage,self.envoi,self.top,self.labelIndication,self.ryleyMenu)
                    if varRyley == 1 :
                        self.phraseAttent()
                    else :
                        if (varRyley != 2):
                            self.sourceRyley.speak("Je peux pas répondre a ta requette "+self.user)



Ryley() 