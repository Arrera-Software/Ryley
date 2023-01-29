from tkinter import*
import webbrowser
import requests
from src.ryleySRC import*
from src.varriable import*
from github import Github
from function.JSON import *
from tkinter import colorchooser
class CodeHelp:
    def __init__(carde,cadre2,entry,label,button,optionMenu,varchoix,nom,oldfnc,labelIndication,mode) :
        screenCode = Toplevel()
        screenCode.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        screenCode.maxsize(500,500)
        screenCode.minsize(500,500)
        screenCode.config(bg=secondColor)
        def resetRyley():
            button.config(command=oldfnc)
            optionMenu.place_forget()
            labelIndication.place_forget()
            entry.place_forget()
            entry.config(width=35)
            entry.place(x="5",y="70")
        def Doc():
            resetRyley()
            CodeHelp.rechercheDoc(carde,entry,label,button,optionMenu,varchoix,nom,oldfnc)
        def github():
            resetRyley()
            CodeHelp.github(carde,entry,label,button,nom,oldfnc,labelIndication)
        def Application():
            bgCode1.pack_forget()
            bgCode2.pack()
            screenCode.title("Ryley : CodeHelp Application")
        def mode1():
            bgCode2.pack_forget()
            bgCode1.pack()
            screenCode.title("Ryley : Code help")
        bgCode1 = Canvas(screenCode,width=500,height=500)
        imgCenter = PhotoImage(file="image/codeHelp/bgCodeHelp.png",master=bgCode1)
        bgCode1.image_names = imgCenter
        bgCode1.create_image(0,0,image=imgCenter,anchor="nw")
        
        bgCode2 = Canvas(screenCode,width=500,height=500)
        imgCenter2 = PhotoImage(file="image/codeHelp/bgCodeHelp.png",master=bgCode2)
        bgCode2.image_names = imgCenter2
        bgCode2.create_image(0,0,image=imgCenter2,anchor="nw")
        if (mode == "1"):
            mode1()
        else :
            if mode == "2":
                Application()
            else :
                mode1()
        buttonDoc = Button(bgCode1,text="Documentation",bg=mainColor,fg=mainTextColor,font=("arial",15),command=Doc	)
        buttonGithub  = Button(bgCode1,text="Connexion à github",bg=mainColor,fg=mainTextColor,font=("arial",15),command=github)
        buttonLibrairy = Button(bgCode1,text="Librairy",bg=mainColor,fg=mainTextColor,)
        buttonApp = Button(bgCode1,text="Application",bg=mainColor,fg=mainTextColor,command=Application)
        buttonColor = Button(bgCode2,text="Selecteur de couleur",bg=mainColor,fg=mainTextColor,command=CodeHelp.ColorSelector)
        buttonVarriable = Button(bgCode2,text="Organisateur de varriable",bg=mainColor,fg=mainTextColor,)
        buttonRetour = Button(bgCode2,text="Retour",bg=mainColor,fg=mainTextColor,command=mode1)
        buttonEditeurDoc = Button(bgCode2,text="Editeur de Doncumentation",bg=mainColor,fg=mainTextColor,)
        
        imgDoc = PhotoImage(file="image/codeHelp/documentation.png",master=buttonDoc)
        imgLibrairy = PhotoImage(file="image/codeHelp/librairy.png",master=buttonLibrairy)
        imgApp = PhotoImage(file="image/codeHelp/application.png",master=buttonApp)
        imgGithub = PhotoImage(file="image/codeHelp/github.png",master=buttonGithub)
        imgColor = PhotoImage(file="image/codeHelp/colorSelector.png",master=buttonColor)
        imgVarriable =PhotoImage(file="image/codeHelp/orgagnisateurVarriable.png",master=buttonVarriable)
        imgRetour = PhotoImage(file="image/codeHelp/retourAririere.png",master=buttonRetour)
        imgEditeurDoc = PhotoImage(file="image/codeHelp/EditeurDoc.png",master=buttonEditeurDoc)
       
        buttonDoc.image_names = imgDoc
        buttonDoc.config(image=imgDoc)
        buttonGithub.image_names = imgGithub
        buttonGithub.config(image=imgGithub)
        buttonLibrairy.image_names = imgLibrairy
        buttonLibrairy.config(image=imgLibrairy)
        buttonApp.image_names = imgApp
        buttonApp.config(image=imgApp)
        buttonColor.image_names = imgColor
        buttonColor.config(image=imgColor)
        buttonVarriable.image_names =imgVarriable
        buttonVarriable.config(image=imgVarriable)
        buttonRetour.image_names = imgRetour
        buttonRetour.config(image=imgRetour)
        buttonEditeurDoc.image_names = imgEditeurDoc
        buttonEditeurDoc.config(image=imgEditeurDoc)
        
        buttonApp.place(x=380,y=200)
        buttonLibrairy.place(x=50,y=200)
        buttonDoc.place(x=220,y=50)
        buttonGithub.place(x=220,y=380)
        buttonColor.place(x=380,y=200)
        buttonVarriable.place(x=50,y=200)
        buttonEditeurDoc.place(x=220,y=50)
        buttonRetour.place(x=220,y=380)
        
    def rechercheDoc(carde,entry,label,button,optionMenu,varchoix,nom,oldfnc):
        RyleySRC.speak("Taper la commande 'help' si tu as besoin d'aide",label,nom) 
        def send():
            url = "https://devdocs.io/#q="
            requette = entry.get()
            if "quitter" in requette:
                entry.delete(0,END)
                entry.place_forget()
                entry.config(width=35)
                entry.place(x="5",y="70")
                RyleySRC.speak("J'espere que sa pu t'etre utile",label,nom)
                label.place(x="10",y="300")
                optionMenu.place_forget()
                button.config(command=oldfnc)
            else :
                if "help" in requette :
                    entry.delete(0,END)
                    label.place(x="10",y="90")
                    label.config(text="Fonction pour faire des recherche directement dans \nl'API DevDocs :\n  -all = Recheche sur tout les docs\n  -python = recherche sur la docs python\n  -javascript = recherche sur la docs javascript\n  -html = recherche sur la docs html \n  -cpp = recherche sur la docs C++\n  -php = recherche sur la docs PHP\n  -openjdk = recherche sur la docs java"
                                 ,justify="left")
                else :
                    entry.delete(0,END)
                    language = varchoix.get()
                    if language == "all":
                        fullUrl = url+requette
                        webbrowser.open(fullUrl)
                    else :
                        fullUrl = url+language+" "+requette
                        webbrowser.open(fullUrl)
        entry.place_forget()
        entry.config(width=25)
        entry.place(x="115",y="70")
        optionMenu.place(x="5",y="70")
        button.config(command=send)
        
    def github(carde,entry,label,button,nom,oldfnc,labelIndication):
        RyleySRC.speak("Taper la commande 'help' si tu as besoin d'aide",label,nom) 
        verifToken = lectureJSON("objet/codeHelp/accessGithub.json","token") != ""
        verifUser = lectureJSON("objet/codeHelp/accessGithub.json","user") != ""
        listRepo = []
        i = 0
        def Quitte():
            entry.delete(0,END)
            entry.place_forget()
            entry.config(width=35)
            entry.place(x="5",y="70")
            label.place(x="10",y="300")
            button.config(command=oldfnc)
            labelIndication.place_forget()
        
        def send():
            requette = str(entry.get())
            entry.delete(0,END)
            if "quitter" in requette :
                label.config(justify="center")
                RyleySRC.speak("J'espere que sa pu t'etre utile",label,nom)
                Quitte()
            else :
                if "liste" in requette :
                    label.config(justify="center")
                    RyleySRC.speak("Tu as "+str(i)+" depot dans ton github\nTaper repos (Le numero) pour voir son nom",label,nom)
                else :
                    if "help" in requette :
                        label.config(text="- Liste : donner le nombre de repos github que tu as\n- search : Faire une recherche dans github\n- repos : afficher le nom d'un repos")
                        entry.delete(0,END)
                        label.config(justify="left")
                    else :
                        if "search" in requette :
                            urlSearch = "https://github.com/search?q="
                            requette = requette.replace("search ","")
                            urllink = requests.get(urlSearch+requette)
                            urllink = urllink.url
                            webbrowser.open(urllink)
                        else :
                            if "repos" in requette :
                                requette = requette.replace("repos ","")
                                requette = int(requette)
                                if requette == 0:
                                    RyleySRC.speak("Tu peux pas avoir ZERO depot",label,nom)
                                else :
                                    requette = requette - 1
                                    RyleySRC.speak("Le nom du depos "+str(requette+1)+" est "+listRepo[requette],label,nom)
                            else :
                                if "open" in requette or "ouvrir" :
                                    RyleySRC.speak("Ok je t'ouvre github",label,nom)
                                    webbrowser.open("https://github.com/")
        labelIndication.config(text="GitHub")
        entry.place_forget()
        entry.config(width=25)
        entry.place(x="115",y="70")
        labelIndication.place(x="5",y="70")
        button.config(command=send)
        if verifToken == True and verifUser == True :
            githubAccess = Github(lectureJSON("objet/codeHelp/accessGithub.json","token"))
            for repo in githubAccess.get_user().get_repos():
                listRepo.append(str(repo.name))
                i = i +1
        else : 
            Quitte()
            RyleySRC.speak("Il n'a pas de token enregistrer taper \n'tokenSave' ou 'userSave pour l'enregister vos information",label,nom)
            button.config(command=oldfnc)
    
    def githubSaveToken(carde,entry,label,button,nom,oldfnc,labelIndication):
        RyleySRC.speak("Taper votre token",label,nom)
        def Save():
            val = str(entry.get())
            entry.delete(0,END)
            EcritureJSON("objet/codeHelp/accessGithub.json","token",val)
            button.config(command=oldfnc)
            RyleySRC.speak("Votre token est enregister",label,nom)
        button.config(command=Save)
        
    def githubSaveUser(carde,entry,label,button,nom,oldfnc,labelIndication):
        RyleySRC.speak("Taper votre nom d'uttilisateur github",label,nom)
        def Save():
            val = str(entry.get())
            entry.delete(0,END)
            EcritureJSON("objet/codeHelp/accessGithub.json","user",val)
            button.config(command=oldfnc)
            RyleySRC.speak("Votre nom d'uttilisateur est enregister",label,nom)
        button.config(command=Save)
        
    def ColorSelector():
        screenColor = Toplevel()
        screenColor.title("Ryley : CodeHelp selecteur de couleur")
        screenColor.config(bg=mainColor)
        screenColor.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        screenColor.maxsize(800,500)
        screenColor.minsize(800,500)
        #fonction
        def selecteur():
            color = colorchooser.askcolor(title="Ryley : CodeHelp selecteur de couleur",color=mainColor)
            colorHTLM = str(color[1])
            colorRGB = str(color[0])
            def CopieHTLM():
                screenColor.clipboard_clear()
                screenColor.clipboard_append(colorHTLM)
            def CopieRGB():
                screenColor.clipboard_clear()
                screenColor.clipboard_append(colorRGB)
            cadreColor.config(bg=colorHTLM)
            buttonCopiHTLM.config(command=CopieHTLM)
            buttonCopiRGB.config(command=CopieRGB)
            labelIndicationCode.config(text="Code HTML : "+colorHTLM+"\nCode RGB : "+colorRGB)
        #cadre
        cadreNoir = Frame(screenColor,bg="black",width=325,height=325,border=100)
        cadreColor = Frame(cadreNoir,bg="#ffffff",width=310,height=310)
        #label
        labelIndicationCode = Label(screenColor,text="Code HTML : #ffffff \nCode RGB : (255,255,255)",bg=mainColor,fg=mainTextColor,font=("arial",15),justify="left")     
        #declaration des bouton
        buttonSelection = Button(screenColor,text="Selectionner la couleur",bg=mainColor,fg=mainTextColor,font=("arial",15),command=selecteur)
        buttonCopiHTLM = Button(screenColor,text="Copier le code HTML",bg=mainColor,fg=mainTextColor,font=("arial",15))
        buttonCopiRGB = Button(screenColor,text="Copier le code RGB",bg=mainColor,fg=mainTextColor,font=("arial",15))
        #affichage
        cadreColor.place(relx=0.5, rely=0.5, anchor=CENTER)
        cadreNoir.pack(side="right")
        labelIndicationCode.place(x=15,y=15)
        buttonSelection.place(x=15,y=135)
        buttonCopiHTLM.place(x=15,y=235)
        buttonCopiRGB.place(x=15,y=335)
        
