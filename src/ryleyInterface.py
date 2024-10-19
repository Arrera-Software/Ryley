from tkinter import*
from src.gestionRyley import*
from librairy.travailJSON import*
from setting.arreraAssistantSetting import*
import time as t
from  ObjetsNetwork.arreraNeuron import*
from librairy.dectectionOS import*
from PIL import Image, ImageTk
from debug.CArreraReturnToolKit import *
from tkinter import scrolledtext

VERSIONAPP = ""
class interfaceRyley:
    def __init__(self,gestionnaire:gestionRL,networkNeuron:ArreraNetwork):
        self.__gestionnaire = gestionnaire
        self.__arreraNetwork = networkNeuron
        self.__objetNetwork = network()
        self.__objetDectOS = OS()
        self.__debugWindows = CArreraReturnToolKit("fichierJSON/debugConf.json")
        self.__dictHist = {}
        self.__reponse = ""
        self.__requette = ""

    def __setTheme(self):
        self.__gestionnaire.setTheme()
        self.__mainColor = self.__gestionnaire.getMaincolor()
        self.__secondColor = self.__gestionnaire.getSecondColor()
        self.__mainTextColor = self.__gestionnaire.getMainTextcolor()
        self.__secondTextColor = self.__gestionnaire.getSecondTextColor()
        self.__BGTop = self.__gestionnaire.getBGTop()
        self.__BGBottom = self.__gestionnaire.getBGBottom()
        self.__BGActu = self.__gestionnaire.getBGActu()
        self.__screen.config(bg=self.__mainColor)
        self.__bgTOP = PhotoImage(file = self.__BGTop)
        self.__bgBOTTOM = PhotoImage(file = self.__BGBottom)
        self.__bgActu = PhotoImage(file=self.__BGActu)
        self.__boutonEnvoyer.configure(bg=self.__secondColor,fg=self.__secondTextColor)
        self.__top.configure(bg=self.__mainColor)
        self.__bottom.configure(bg=self.__secondColor)
        self.__btnBackActu.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        self.__actu.configure(bg=self.__mainColor)
        self.__actu.create_image( 0, 0, image = self.__bgActu, anchor = "nw")
        self.__top.create_image( 0, 0, image = self.__bgTOP, anchor = "nw")
        self.__bottom.create_image( 0, 0, image = self.__bgBOTTOM, anchor = "nw")
        self.__labelResumer.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        self.__labelParole.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        self.__ryleyMenu.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        self.__objetSetting = ArreraSettingAssistant("fichierJSON/configSetting.json"
                                                     ,"fichierJSON/configNeuron.json"
                                                     ,"fichierJSON/ryleyConfig.json"
                                                     ,"fichierJSON/configUser.json")
    
    def windows(self):
        #Definition fenetre Tkinter
        self.__screen = Tk()
        self.__iconWindows = PhotoImage(file="asset/Ryley.png")
        #Parametre Interface
        self.__screen.title("Ryley")
        if (OS().osLinux() == True):
            self.__screen.maxsize(500,635)
            self.__screen.minsize(500,635)
        else :
            self.__screen.maxsize(500,610)
            self.__screen.minsize(500,610)
        self.__screen.iconphoto(False,self.__iconWindows)
        #Canvas
        self.__top = Canvas( self.__screen, width = 500,height = 400, highlightthickness=0)
        self.__bottom = Canvas( self.__screen, width = 500,height = 200, highlightthickness=0)
        self.__actu =  Canvas( self.__screen, width = 500,height = 600, highlightthickness=0)
        #Label
        self.__labelParole = Label(self.__top,text="Ryley "+": "+self.__arreraNetwork.boot(2),font=("arial","14"), justify="left",wraplength=450)
        self.__labelResumer = Label(self.__actu,font=("arial","14"), justify="left",wraplength=400)
        #button
        self.__btnBackActu = Button(self.__actu,text="Retour",command=self.__unViewActu,font=("arial","15"))
        #Menu
        #Creation menu principale
        self.__ryleyMenu = Menu(self.__screen)
        #Creation menu secondaire
        self.__fichierMenu = Menu(self.__ryleyMenu,tearoff=0)
        helpMenu = Menu(self.__ryleyMenu,tearoff=0)
        debugMenu = Menu(self.__ryleyMenu,tearoff=0)
        #Ajout des command au menu fichierMenu
        self.__fichierMenu.add_command(label="Paramétre",command=self.__activePara)
        self.__fichierMenu.add_command(label="Test de connexion",command=self.__windowsEtatNetwork)
        self.__fichierMenu.add_command(label="Calculatrice",command=self.__ouvertureCalculatrice)
        # Menu debugMenu
        debugMenu.add_command(label="Documentation",
                              command=lambda : webbrowser.open("https://github.com/Arrera-Documentation/Ryley-doc/blob/master/Writerside/topics/Documentation.md"))
        debugMenu.add_command(label="Instruction beta testeur")
        debugMenu.add_command(label="Historique requette/reponse",command=self.__windowsHist)
        #Ajout des command au menu helpMenu
        helpMenu.add_command(label="Documentation")
        helpMenu.add_command(label="A propos")
        #Ajout au menu principale tout les menu deroulant      
        self.__ryleyMenu.add_cascade(label="Fichier",menu=self.__fichierMenu)
        self.__ryleyMenu.add_cascade(label="Aide",menu=helpMenu)
        self.__ryleyMenu.add_cascade(label="Debug",menu=debugMenu)
        self.__ryleyMenu.add_command(label="Reporter au developpeur", command=lambda: self.__debugWindows.active())
        self.__ryleyMenu.add_command(label="A propos",command=self.__Apropop)
        #parametrage parametre
        self.__boutonEnvoyer=Button(self.__bottom,text="Envoyer",font=("arial","15"),command=self.__envoi)
        #Application du theme
        self.__setTheme()
        #Afichage
        self.__barreR = Entry(self.__bottom,width=35,font=("arial","15"),relief=SOLID)
        self.__labelParole.place(x="10",y="300")
        self.__labelResumer.place(x="80",y="5")
        self.__barreR.place(x="5",y="70")
        self.__boutonEnvoyer.place(x="400",y="65")
        self.__btnBackActu.place(x=((self.__actu.winfo_reqwidth()-self.__btnBackActu.winfo_reqwidth())//2),y="520")
    
    
    def bootRyley(self):
        self.__top.place(x=0,y=0)
        self.__bottom.place(x=0,y=400)
        self.__objetSetting.passageFonctionQuitter(self.__desactiverPara)
        if (self.__objetDectOS.osWindows()==True) and (self.__objetDectOS.osLinux()==False) : 
            self.__gestionnaire.detectionTouche(self.__screen,self.__envoi,13)
        else :
            if (self.__objetDectOS.osWindows()==False) and (self.__objetDectOS.osLinux()==True) :
                self.__gestionnaire.detectionTouche(self.__screen,self.__envoi,36)
        self.__screen.configure(menu=self.__ryleyMenu)
        self.__screen.update()

    def bootPara(self):
        def destroyWin():
            self.__screen.destroy()
        self.__top.place_forget()
        self.__bottom.place_forget()
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__screen.update()
        self.__objetSetting.passageFonctionQuitter(destroyWin)
        self.__objetSetting.windows(self.__screen)
        self.__objetSetting.mainView() 
        self.__screen.mainloop()
    

    def __activePara(self):
        #fichierConfigSetting = jsonWork("fichierJSON/configSetting.json")
        #fichierConfigSetting.EcritureJSON("color1",self.__mainColor)
        self.__top.place_forget()
        self.__bottom.place_forget()
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__objetSetting.passageFonctionQuitter(self.__desactiverPara)
        self.__fichierMenu.entryconfigure("Paramétre",label="Acceuil",command=self.__objetSetting.quittePara)
        self.__screen.update()
        self.__objetSetting.windows(self.__screen,self.__gestionnaire.getThemeMode())
        self.__objetSetting.mainView() 
        self.__screen.mainloop()
        
    def __viewResumer(self,sortie:list,valeur:int):
        self.__top.place_forget()
        self.__bottom.place_forget()
        self.__actu.place(x=0,y=0)
        if (valeur==3):
            self.__labelResumer.configure(text=sortie[0]+"\n\n"+sortie[1]+"\n\n"+sortie[2])
        else :
            if ((valeur == 11) or (valeur == 20)):
                self.__actu.place_forget()
                self.__top.place(x=0,y=0)
                self.__bottom.place(x=0,y=400)
                self.__setText("Une erreur c'est produite")
            else :
                if (valeur == 12) :
                    if (sortie[0] == "error"):
                        self.__labelResumer.configure(text=sortie[1]+"\n La fete du jour est : "+sortie[2]+"\n"+sortie[3]+"\n"+sortie[4]+"\n\n"+sortie[5])
                    else :
                        self.__labelResumer.configure(text=sortie[0]+"\n"+sortie[1]+"\n La fete du jour est : "+sortie[2]+"\n"+sortie[3]+"\n"+sortie[4]+"\n\n"+sortie[5])
                else :
                    if (valeur == 19):
                        self.__setText(sortie[6])
                        if sortie[0] == "error":
                            self.__labelResumer.configure(text=sortie[1]+"\nFête du jour : "+sortie[2]+"\n"+sortie[3]+"\n"+sortie[4]+"\n"+sortie[5]+"\n"+sortie[7]+"\n"+sortie[8])
                        else :
                            self.__labelResumer.configure(text=sortie[0]+"\n"+sortie[1]+"\nFête du jour : "+sortie[2]+"\n"+sortie[3]+"\n"+sortie[4]+"\n"+sortie[5]+"\n"+sortie[7]+"\n"+sortie[8])
                    else :
                        if (valeur==18):
                            self.__setText("J'espère que se résumé ta bien aider")
                            self.__labelResumer.configure(text=sortie[0]+"\n"+sortie[1])
                        
    
    def __unViewActu(self):
        self.__actu.place_forget()
        self.__top.place(x=0,y=0)
        self.__bottom.place(x=0,y=400)
    
    def __desactiverPara(self):
        #Application du theme
        self.__setTheme()
        self.__screen.update()
        self.__top.place(x=0,y=0)
        self.__bottom.place(x=0,y=400)
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__fichierMenu.entryconfigure("Acceuil",label="Paramétre",command=self.__activePara)
        
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

    def __envoi(self):
        statement = self.__barreR.get()
        self.__barreR.delete("0",END)
        var = 0 
        self.__arreraNetwork.neuron(statement)
        listOut = self.__arreraNetwork.getListSortie()
        var = self.__arreraNetwork.getValeurSortie()
        if (var == 12 or var == 11):
            self.setHist("resumer",statement)
            self.__viewResumer(listOut,var)
        else :
            if ((var == 3) or (var == 12) or (var == 18) or (var == 19)) :
                self.setHist("resumer",statement)
                self.__viewResumer(listOut,var)
            else :
                if (var == 17):
                    self.setHist("help",statement)
                    self.__windowsHelp(listOut)
                else :
                    texte = listOut[0]
                    self.setHist(texte,statement)
                    self.__setText(texte)
        if var == 15 :
            self.__screen.update()
            t.sleep(1.5)
            self.__screen.destroy()
    
    def __ouvertureCalculatrice(self):
        self.__arreraNetwork.neuron("calculatrice")
        texte = self.__arreraNetwork.getListSortie()[0]
        self.__setText(texte)
    
    def __setText(self,texte:str):
        self.__labelParole.configure(text="Ryley "+": "+texte)

    def __Apropop(self):
        #Variable
        nameApp = "Ryley"#Definir le nom de l'app
        versionApp = VERSIONAPP
        imagePath = "asset/Ryley.png"#Indiquer l'emplacement de l'icon
        copyrightApp = "Copyright Arrera Software by Baptiste P 2023-2024"
        tailleIMG = (100,100)
        #Creation de la fenetre
        about = Tk()
        about.title("A propos : "+nameApp)
        about.configure(bg=self.__mainColor)
        about.maxsize(400,300)
        about.minsize(400,300)
        #Traitement Image
        imageOrigine = Image.open(imagePath)    
        imageRedim = imageOrigine.resize(tailleIMG)
        icon = ImageTk.PhotoImage(imageRedim)
        #Label
        labelIcon = Label(about,bg=self.__mainColor,fg=self.__mainTextColor)
        icon = ImageTk.PhotoImage(imageRedim,master=labelIcon)
        labelIcon.image_names = icon
        labelIcon.configure(image=icon)
        labelName = Label(about,text="\n"+nameApp+"\n",font=("arial","12"),bg=self.__mainColor,fg=self.__mainTextColor)
        labelVersion = Label(about,text=versionApp+"\n",font=("arial","11"),bg=self.__mainColor,fg=self.__mainTextColor)
        labelCopyright = Label(about,text=copyrightApp,font=("arial","9"),bg=self.__mainColor,fg=self.__mainTextColor)
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()
        about.mainloop()
    
    def __windowsHelp(self,list:list):
        texte = list[0]
        winHelp = Toplevel()
        winHelp.title("Ryley : Aide")
        winHelp.iconphoto(False,self.__iconWindows)
        winHelp.configure(bg=self.__mainColor)
        if (list[1]=="tableur"):
            if (OS().osLinux() == True):
                winHelp.maxsize(800,835)
                winHelp.minsize(800,835)
            else :
                winHelp.maxsize(800,810)
                winHelp.minsize(800,810)
            warp = 795
            self.__setText("Je t'ai ouvert une fenêtre avec tout ce que tu peux faire avec un fichier tableur.")
        else :
            if (list[1]=="word"):
                if (OS().osLinux() == True):
                    winHelp.maxsize(600,635)
                    winHelp.minsize(600,635)
                else :
                    winHelp.maxsize(600,610)
                    winHelp.minsize(600,610)
                warp = 580
                self.__setText("Voici la fenêtre d'aide pour la gestion des fichiers de traitement de texte avec moi.")
            else :
                if (list[1]== "fichier" or list[1] == "radio"):
                    if (OS().osLinux() == True):
                        winHelp.maxsize(500,635)
                        winHelp.minsize(500,635)
                    else :
                        winHelp.maxsize(500,610)
                        winHelp.minsize(500,610)
                    warp = 450
                    match list[1] :
                        case "fichier" :
                            self.__setText("Je t'ai ouvert une fenêtre avec la liste de tous les fichiers que je peux créer dans un projet.")
                        case "radio" :
                            self.__setText("Voici la liste des radios que je peux te lancer à l'écoute.")
                else :
                    if (list[1]=="projet"):
                        if (OS().osLinux() == True):
                            winHelp.maxsize(1050,890)
                            winHelp.minsize(1050,890)
                        else :
                            winHelp.maxsize(1050,865)
                            winHelp.minsize(1050,865)
                        self.__setText("Je t'ai ouvert une fenêtre avec toutes les fonctions du projet Arrera.")
                        warp = 1040
        
        labelHelp = Label(winHelp,text=texte,wraplength=warp,font=("arial","15"),
                          bg=self.__mainColor,fg=self.__mainTextColor,justify="left")
        
        labelHelp.place(x=0,y=0)

    def setHist(self,reponse:str,requette:str):
        if (reponse and requette):
            self.__dictHist[requette] = reponse
            self.__requette = requette
            self.__reponse = reponse
            return  True
        else :
            return False

    def __windowsHist(self):
        if (self.__requette and self.__reponse ):
            # Declaration de la fentre
            win = Toplevel()
            if (OS().osLinux() == True):
                width=500
                height = 635
            else:
                width = 500
                height = 610
            win.minsize(width, height)
            win.maxsize(width, height)
            # Declaration des frame
            ftext = Frame(win, bg=self.__mainColor, width=width, height=height - 40)
            fbottom = Frame(win, bg=self.__mainColor, width=width, height=40)
            # Zone de texte avec défilement
            histView = scrolledtext.ScrolledText(ftext, wrap=WORD)
            # Bouton dans le frame du bas
            btnCopy = Button(fbottom, bg=self.__mainColor, fg=self.__mainTextColor,
                             text="Copier le dernier échange", font=("arial", "15"),command=self.__copyLastEchange)
            # Ajout de l'historique dans histView
            histView.config(state=NORMAL)
            histView.delete(1.0, END)
            for index, valeur in self.__dictHist.items():
                histView.insert(END, f'Requette :"{index}"\nReponse :"{valeur}"\n\n')
            histView.config(state=DISABLED)
            # Placement des wigdet et des frame
            histView.pack(padx=10, pady=10, fill=BOTH, expand=True)
            btnCopy.place(relx=0.5, rely=0.5, anchor="center")
            # Pack les frames
            ftext.pack(side="top", fill=BOTH, expand=True)  # Ajustement automatique de ce frame
            fbottom.pack(side="bottom", fill=X)

            return True
        else :
            return False

    def __copyLastEchange(self):
        pyperclip.copy("Requette : "+self.__requette+"\nReponse : "+self.__reponse)
        showinfo("Ryley","Dernier echange avec Ryley copier")
