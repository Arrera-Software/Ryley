from tkinter import*
import webbrowser
import requests
from src.ryleySRC import*
from src.varriable import*
class CodeHelp:
    def __init__(carde,cadre2,entry,label,button,optionMenu,varchoix,nom,oldfnc) :
        screenCode = Toplevel()
        screenCode.title("Ryley : Code help")
        screenCode.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        screenCode.maxsize(500,500)
        screenCode.minsize(500,500)
        screenCode.config(bg=secondColor)
        bgCode = Canvas(screenCode,width=500,height=500)
        imgCenter = PhotoImage(file="image/codeHelp/bgCodeHelp.png",master=bgCode)
        bgCode.image_names = imgCenter
        bgCode.create_image(0,0,image=imgCenter,anchor="nw")
        buttonDoc = Button(screenCode,text="Documentation",bg=mainColor,fg=mainTextColor,font=("arial",15))
        imgDoc = PhotoImage(file="image/codeHelp/documentation.png",master=buttonDoc)
        buttonDoc.image_names = imgDoc
        buttonDoc.config(image=imgDoc)
        buttonGithub  = Button(screenCode,text="Connexion à github",bg=mainColor,fg=mainTextColor,font=("arial",15))
        imgGithub = PhotoImage(file="image/codeHelp/github.png",master=buttonGithub)
        buttonGithub.image_names = imgGithub
        buttonGithub.config(image=imgGithub)
        buttonDoc.place(x=220,y=50)
        buttonGithub.place(x=220,y=380)
        bgCode.pack()
        
    def rechercheDoc(carde,entry,label,button,optionMenu,varchoix,nom,oldfnc):
        def send():
            url = "https://devdocs.io/#q="
            requette = entry.get()
            if requette == "quitter":
                entry.delete(0,END)
                entry.place_forget()
                entry.config(width=35)
                entry.place(x="5",y="70")
                RyleySRC.speak("J'espere que sa pu t'etre utile",label,nom)
                label.place(x="10",y="300")
                optionMenu.place_forget()
                button.config(command=oldfnc)
            else :
                if requette == "help" :
                    entry.delete(0,END)
                    label.place(x="10",y="90")
                    label.config(text="Fonction pour gaire des recherche directement dans \nl'API DevDocs :\n  -all = Recheche sur tout les docs\n  -python = recherche sur la docs python\n  -javascript = recherche sur la docs javascript\n  -html = recherche sur la docs html \n  -cpp = recherche sur la docs C++\n  -php = recherche sur la docs PHP\n  -openjdk = recherche sur la docs java"
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
    
    
        
        
             