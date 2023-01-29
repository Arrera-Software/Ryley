from tkinter import*
import webbrowser
import requests
from src.ryleySRC import*
from src.varriable import*
from github import Github
from function.JSON import *
class CodeHelp:
    def __init__(carde,cadre2,entry,label,button,optionMenu,varchoix,nom,oldfnc,labelIndication) :
        screenCode = Toplevel()
        screenCode.title("Ryley : Code help")
        screenCode.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        screenCode.maxsize(500,500)
        screenCode.minsize(500,500)
        screenCode.config(bg=secondColor)
        def Doc():
            CodeHelp.rechercheDoc(carde,entry,label,button,optionMenu,varchoix,nom,oldfnc)
        def github():
            CodeHelp.github(carde,entry,label,button,nom,oldfnc,labelIndication)
        bgCode = Canvas(screenCode,width=500,height=500)
        imgCenter = PhotoImage(file="image/codeHelp/bgCodeHelp.png",master=bgCode)
        bgCode.image_names = imgCenter
        bgCode.create_image(0,0,image=imgCenter,anchor="nw")
        buttonDoc = Button(screenCode,text="Documentation",bg=mainColor,fg=mainTextColor,font=("arial",15),command=Doc	)
        imgDoc = PhotoImage(file="image/codeHelp/documentation.png",master=buttonDoc)
        buttonDoc.image_names = imgDoc
        buttonDoc.config(image=imgDoc)
        buttonGithub  = Button(screenCode,text="Connexion à github",bg=mainColor,fg=mainTextColor,font=("arial",15),command=github)
        imgGithub = PhotoImage(file="image/codeHelp/github.png",master=buttonGithub)
        buttonGithub.image_names = imgGithub
        buttonGithub.config(image=imgGithub)
        buttonLibrairy = Button(screenCode,text="Librairy")
        imgLibrairy = PhotoImage(file="image/codeHelp/librairy.png",master=buttonLibrairy)
        buttonLibrairy.image_names = imgLibrairy
        buttonLibrairy.config(image=imgLibrairy)
        buttonApp = Button(screenCode,text="Application")
        imgApp = PhotoImage(file="image/codeHelp/application.png",master=buttonApp)
        buttonApp.image_names = imgApp
        buttonApp.config(image=imgApp)
        buttonApp.place(x=380,y=200)
        buttonLibrairy.place(x=50,y=200)
        buttonDoc.place(x=220,y=50)
        buttonGithub.place(x=220,y=380)
        bgCode.pack()
        
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
        
    
    
        
        
             