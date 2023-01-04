import webbrowser
import os
import datetime
import random
from tkinter.messagebox import showinfo
import time
#file
from function.JSON import*
from setting.setting import*
from function.internet import*
from src.parole import*
from function.traduction import*
from API.API import*
from varriable import*
from neuron.neuronMain import*
#Var
nameAssistant = lectureJSON("setting/config.json","nomAssistant")
User = lectureJSON("setting/config.json","user")
#Definition fenetre Tkinter
screen = Tk()
bgTOP = PhotoImage(file = "image/BGTop.png")
bgBOTTOM = PhotoImage(file = "image/BGBottom.png")
screen.title("Ryley")
screen.config(bg=mainColor)
screen.maxsize(500,600)
screen.minsize(500,600)
screen.iconphoto(False,PhotoImage(file="image/Ryley.png"))
top = Canvas( screen, width = 500,height = 400)
top.pack()
top.create_image( 0, 0, image = bgTOP, anchor = "nw")
bottom = Canvas( screen, width = 500,height = 200)
bottom.pack(side="bottom")
bottom.create_image( 0, 0, image = bgBOTTOM, anchor = "nw")
labelParole = Label(top,text=nameAssistant+":",bg=mainColor,fg=mainTextColor,font=("arial","14"))
#Fonction

def APropos():
    screenAPropos = Toplevel()
    screenAPropos.title("Ryley")
    screenAPropos.maxsize(425,170)
    screenAPropos.minsize(425,170)
    screenAPropos.iconphoto(False,PhotoImage(file="image/Ryley.png"))
    screenAPropos.config(bg=mainColor)
    Label(screenAPropos,text="Assistant Personnelle Ryley\nCréer par:\nSpeedyCreator\net\nWiruto2",font=("arial","20"),bg=mainColor,fg=mainTextColor).pack()

def Introduction():
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour <=5:
        speak("Zzzz "+User+" Il faut peut etre dormir non?",labelParole,nameAssistant)
    if hour >= 6 and hour <= 9 :
        speak("Hey "+User+" as-tu bien dormi?",labelParole,nameAssistant)
    if hour >= 10 and hour <= 12:
        speak("Salut "+User+" comment ce passe ta matinée?",labelParole,nameAssistant)
    if hour >= 13 and hour <= 17:
        speak("Alors "+User+" pret a travailler?",labelParole,nameAssistant)
    if hour >= 18 and hour <= 23:
        speak("*baille* "+User+" ? Que fais tu si tard?",labelParole,nameAssistant)

#Menu
ryleyMenu = Menu(screen,bg="white",fg="black")
fichierMenu = Menu(ryleyMenu,tearoff=0)
fichierMenu.add_command(label="Paramétre",command=Setting)
fichierMenu.add_command(label="Test Internet",command=TestInternet)
ryleyMenu.add_cascade(label="Fichier",menu=fichierMenu)
ryleyMenu.add_command(label="A propos",command=APropos)
screen.config(menu=ryleyMenu)
#Code principal
Introduction()
barreR = Entry(bottom,width=35,font=("arial","15"))
def envoi():
    requete=str(barreR.get())
    varRyley = Main(requete,screen,User,labelParole,nameAssistant)
    if varRyley == 1 :
        print()
    else :
        speak("Je peux pas répondre a ta requette "+User,labelParole,nameAssistant)
   
boutonEnvoyer=Button(bottom,text="Envoyer",command=envoi,bg=secondColor,fg=secondTextColor,font=("arial","15"))
#Affichage
labelParole.place(x="10",y="300")
barreR.place(x="5",y="130")
boutonEnvoyer.place(x="400",y="125")
#Fin de la boucle
screen.mainloop()