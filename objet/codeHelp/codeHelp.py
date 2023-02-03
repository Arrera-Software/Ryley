from tkinter import*
import webbrowser
import requests
from src.ryleySRC import*
from src.varriable import*
from function.opensoft import*
from github import Github
from function.JSON import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
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
        buttonEditeurDoc = Button(bgCode2,text="Editeur de Doncumentation",bg=mainColor,fg=mainTextColor,command=CodeHelp.EditeurDoc)
        
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
        verifToken = lectureJSON("objet/codeHelp/codehelp.json","token") != ""
        verifUser = lectureJSON("objet/codeHelp/codehelp.json","user") != ""
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
            githubAccess = Github(lectureJSON("objet/codeHelp/codehelp.json","token"))
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
            EcritureJSON("objet/codeHelp/codehelp.json","token",val)
            button.config(command=oldfnc)
            RyleySRC.speak("Votre token est enregister",label,nom)
        button.config(command=Save)
        
    def githubSaveUser(carde,entry,label,button,nom,oldfnc,labelIndication):
        RyleySRC.speak("Taper votre nom d'uttilisateur github",label,nom)
        def Save():
            val = str(entry.get())
            entry.delete(0,END)
            EcritureJSON("objet/codeHelp/codehelp.json","user",val)
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
        
    def EditeurDoc():
        screenEditDoc = Toplevel()
        
        def new():
            nbTemplate =  lectureJSON("objet/codeHelp/codehelp.json","nbTemplate")
            zoneText.delete("1.0", END)
            if nbTemplate == "1":
                file = "objet/codeHelp/template/template1.docCode"  
            else :
                if nbTemplate == "2":
                    file = "objet/codeHelp/template//template2.docCode" 
                else :
                    file = "objet/codeHelp/template/template3.docCode"     
            if file:
                with open(file, "r") as f:
                    zoneText.delete("1.0", END)
                    zoneText.insert(INSERT, f.read())
        def sauvegarde ():
            file = filedialog.asksaveasfilename(defaultextension=".docCode", filetypes=[("Documentation", ".docCode"),("All Files", "*.*")])
            if file:
                # Sauvegarder le contenu du fichier
                with open(file, "w") as f:
                    f.write(zoneText.get("1.0", "end"))
                    f.close()
        def openfile():
            file = askopenfilename(defaultextension=".docCode", filetypes=[("Documentation", ".docCode"),("All Files", "*.*")])
            if file:
                with open(file, "r") as f:
                    zoneText.delete("1.0", END)
                    zoneText.insert(INSERT, f.read())
        
        def AllClear():
            labelAide.pack_forget()
            boutonExit.pack_forget()
            labelFonction.pack_forget()
            boutonOpen.pack_forget()
            cadreTemplate.place_forget()
            cadreCSS.place_forget()
            boutonExit.pack_forget()
            
        def help():
            AllClear()
            zoneText.grid_forget()
            labelAide.pack()
            boutonExit.pack(side="bottom")
            boutonOpen.pack(side="right")
            labelFonction.pack(side="left",anchor="n")
            def exit():
                labelAide.pack_forget()
                boutonExit.pack_forget()
                boutonOpen.pack_forget()
                labelFonction.pack_forget()
                zoneText.grid(row=0, column=0, sticky='nsew')
            def buttonHelp():
                openSoft("objet/codehelp/EditeurDoc/help.html")
            boutonExit.config(command=exit)
            boutonOpen.config(command=buttonHelp)
        
        def template():
            AllClear()
            zoneText.grid_forget()
            cadreTemplate.place(relx=0.5, rely=0.5, anchor=CENTER)
            def exit():
                cadreTemplate.place_forget()
                boutonExit.pack_forget()
                zoneText.grid(row=0, column=0, sticky='nsew')
            def select1():
                EcritureJSON("objet/codeHelp/codehelp.json","nbTemplate","1")
                exit()
                new()
            def select2():
                EcritureJSON("objet/codeHelp/codehelp.json","nbTemplate","2")
                exit()
                new()
            def select3():
                EcritureJSON("objet/codeHelp/codehelp.json","nbTemplate","3")
                exit()
                new()
            buttonTemplate1.config(command=select1)
            buttonTemplate2.config(command=select2)
            buttonTemplate3.config(command=select3)
            boutonExit.pack(side="bottom")
            boutonExit.config(command=exit)
        def convers():
            AllClear()
            def exit():
                cadreCSS.place_forget()
                zoneText.grid(row=0, column=0, sticky='nsew')
            fileHTML = open("objet/codeHelp/EditeurDoc/base.html","r")
            texte = zoneText.get("1.0", END)
            texte = texte.replace(">","")
            texte = texte.replace("<","")
            texte =texte.replace("£","<h1>")
            texte =texte.replace("+","<h1 id='titreGras'>")
            texte =texte.replace("@","<h1 id='titreSouligner'>")
            texte =texte.replace("$","</h1>")
            texte =texte.replace("&",'<p>')
            texte =texte.replace("%","<p id='texteSouligner'>")
            texte =texte.replace("µ","<p id='texteGras'>")
            doc = fileHTML.read()
            finHTML = "</body>\n<div id='copieright'><p>Documentation cree avec le logiciel Ryley CodeHelp</p>\n<p>Arrera Software par Baptiste Pauchet</p></div></html>"
            doc = doc+texte+finHTML
            file = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("page HTML", ".html"),("All Files", "*.*")])
            with open(file, "w") as f:
                f.write(doc)
                f.close()
            zoneText.grid_forget()
            cadreCSS.place(relx=0.5, rely=0.5, anchor=CENTER)
            def Selet1():
                with open("objet/codeHelp/EditeurDoc/style1.css", "r") as f:
                    css = f.read()
                    showinfo(title="Ryley : CodeHelp Editeur de documentation",message="Si vous nommer pas votre fichier style.css\nVotre documentation ne sera moche")
                    fileCSS = filedialog.asksaveasfilename(defaultextension="style.css", filetypes=[("Fichier CSS", "style.css")])
                    with open(fileCSS, "w") as f:
                        f.write(css)
                        f.close()
                exit()
            def Selet2():
                with open("objet/codeHelp/EditeurDoc/style2.css", "r") as f:
                    css = f.read()
                    showinfo(title="Ryley : CodeHelp Editeur de documentation",message="Si vous nommer pas votre fichier style.css\nVotre documentation ne sera moche")
                    fileCSS = filedialog.asksaveasfilename(defaultextension="style.css", filetypes=[("Fichier CSS", "style.css")])
                    with open(fileCSS, "w") as f:
                        f.write(css)
                        f.close()
                exit()
            def Selet3():
                with open("objet/codeHelp/EditeurDoc/style3.css", "r") as f:
                    css = f.read()
                    showinfo(title="Ryley : CodeHelp Editeur de documentation",message="Si vous nommer pas votre fichier style.css\nVotre documentation ne sera moche")
                    fileCSS = filedialog.asksaveasfilename(defaultextension="style.css", filetypes=[("Fichier CSS", "style.css")])
                    with open(fileCSS, "w") as f:
                        f.write(css)
                        f.close()
                exit()
            buttonCSS1.config(command=Selet1)  
            buttonCSS2.config(command=Selet2)
            buttonCSS3.config(command=Selet3)
             
        screenEditDoc.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        screenEditDoc.title("Ryley : CodeHelp Editeur de documentation")
        screenEditDoc.columnconfigure(0, weight=1)
        screenEditDoc.rowconfigure(0, weight=1)
        screenEditDoc.minsize(800,500)
        screenEditDoc.config(bg=mainColor)
        menuTop = Menu(screenEditDoc,bg=mainColor,fg=mainTextColor)
        screenEditDoc.config(menu=menuTop)
        menuTop.add_command(label="Nouveau",command=new)
        menuTop.add_command(label="Ouvrir",command=openfile)
        menuTop.add_command(label="Sauvegarder",command=sauvegarde)
        menuTop.add_command(label="Template",command=template)
        menuTop.add_command(label="Convertir en HTML",command=convers)
        menuTop.add_command(label="Aide",command=help)
        #cadre
        cadreTemplate = Frame(screenEditDoc,bg=mainColor,width=775,height=400)
        cadreCSS = Frame(screenEditDoc,bg=mainColor,width=775,height=400)
        #label
        labelAide = Label(screenEditDoc,text="Arrera Ryley CodeHelp Editeur de documentation",bg=mainColor,fg=mainTextColor,font=("arial",15))
        labelFonction = Label(screenEditDoc,text="\n\nFonction : \n\n- £><$ = Titre\n\n- +><$ = Titre en gras\n\n- @><$ = Titre souligner\n\n- %><# = Texte souligner\n\n- &><# = Texte normale\n\n- µ><# = Texte en gras",bg=mainColor,fg=mainTextColor,font=("arial",15),justify="left")
        labelTemplate1 = Label(cadreTemplate,bg="black",fg="white",font=("arial",12),justify="left",text="Introduction :\n\nInstallation et configuration :\n\nFonction :\n")
        labelTemplate2 = Label(cadreTemplate,bg="black",fg="white",font=("arial",12),justify="left",text="Introduction :\n\nInstallation et configuration :\n\nInterface utilisateur :\n\nFonction :")    
        labelTemplate3 = Label(cadreTemplate,bg="black",fg="white",font=("arial",12),justify="left",text="Introduction :\n\nInstallation et configuration :\n\nInterface utilisateur :\n\nFonction :\n\nConnextion API :\n\nLien vers d'autres resources:")
        labelCSS1 = Label(cadreCSS,bg="black",fg="white",font=("arial",12),justify="left",text="- Couleur de fond : Blanc\n- Couleur de text : Noir")
        labelCSS2 = Label(cadreCSS,bg="black",fg="white",font=("arial",12),justify="left",text="- Couleur de fond : Noir\n- Couleur de text : blanc")
        labelCSS3 = Label(cadreCSS,bg="black",fg="white",font=("arial",12),justify="left",text="- Couleur de fond : bleu\n- Couleur de text : blanc")
        #button
        boutonExit = Button(screenEditDoc,text="Exit",bg=mainColor,fg=mainTextColor,font=("arial",15))
        boutonOpen = Button(screenEditDoc,text="Ouvrir le fichier d'aide",bg=mainColor,fg=mainTextColor,font=("arial",15))
        buttonTemplate1 = Button(cadreTemplate,text="Select",bg=mainColor,fg=mainTextColor,font=("arial",15))
        buttonTemplate2 = Button(cadreTemplate,text="Select",bg=mainColor,fg=mainTextColor,font=("arial",15))
        buttonTemplate3 = Button(cadreTemplate,text="Select",bg=mainColor,fg=mainTextColor,font=("arial",15))
        buttonCSS1 = Button(cadreCSS,text="Select",bg=mainColor,fg=mainTextColor,font=("arial",15))
        buttonCSS2 = Button(cadreCSS,text="Select",bg=mainColor,fg=mainTextColor,font=("arial",15))
        buttonCSS3 = Button(cadreCSS,text="Select",bg=mainColor,fg=mainTextColor,font=("arial",15))
        #zone de text
        zoneText = Text(screenEditDoc,font=("arial",15))
        new()
        #affichage
        zoneText.grid(row=0, column=0, sticky='nsew')
        labelTemplate1.place(x=0,y=0)
        labelTemplate2.place(x=275,y=0)
        labelTemplate3.place(x=550,y=0)
        buttonTemplate1.place(x=50,y=350)
        buttonTemplate2.place(x=325,y=350)
        buttonTemplate3.place(x=600,y=350)
        labelCSS1.place(x=0,y=0)
        labelCSS2.place(x=275,y=0)
        labelCSS3.place(x=550,y=0)
        buttonCSS1.place(x=50,y=350)
        buttonCSS2.place(x=325,y=350)
        buttonCSS3.place(x=600,y=350)
        
