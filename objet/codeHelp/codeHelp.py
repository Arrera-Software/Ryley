from tkinter import*
import webbrowser
import requests
from src.ryleySRC import*
class CodeHelp:
    def rechercheDoc(carde,entry,label,button,optionMenu,varchoix,nom,oldfnc):
        url = "https://devdocs.io/#q="
        def send():
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
        
        
             