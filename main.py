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
from src.micro import*
from neuron.neuronSearch import*
#Var
nameAssistant = lectureJSON("setting/config.json","nomAssistant")
user = lectureJSON("setting/config.json","user")
#Definition fenetre Tkinter
screen = Tk()
bgTOP = PhotoImage(file = "image/BGTop.png")
bgBOTTOM = PhotoImage(file = "image/BGBottom.png")
imgMicro = PhotoImage(file="image/imgMicro.png")
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
        speak("Zzzz "+user+" Il faut peut etre dormir non?",labelParole,nameAssistant)
    else :
        if hour >= 6 and hour <= 9 :
            speak("Hey "+user+" as-tu bien dormi?",labelParole,nameAssistant)
        else :
            if hour >= 10 and hour <= 12:
                speak("Salut "+user+" comment ce passe ta matinée?",labelParole,nameAssistant)
            else :
                if hour >= 13 and hour <= 17:
                    speak("Alors "+user+" pret a travailler?",labelParole,nameAssistant)
                else :
                    if hour >= 18 and hour <= 21 :
                        speak("Alors "+user+"que veut-tu faire ce soir ?",labelParole,nameAssistant)
                    else :
                        if hour >= 22 and hour <= 23:
                            speak("*baille* "+user+" ? Que fais tu si tard?",labelParole,nameAssistant)
                        else :
                            speak("Salut "+user,labelParole,nameAssistant)
def phraseAttent():
    nbrad = random.randrange(1,6)
    if nbrad == 1 :
        speak("En quoi je peux d'aider "+user,labelParole,nameAssistant)
    else :
        if nbrad == 2 :
            speak("J'espére que j'ai pu d'aider "+user,labelParole,nameAssistant)
        else :
           if nbrad == 3 :
                speak("En quoi je peux encore d'aider "+user,labelParole,nameAssistant) 
           else :
               if nbrad == 4 :
                    speak("Je peux encore plus d'aider "+user,labelParole,nameAssistant)
               else :
                   if nbrad == 5 :
                        speak("Dit-moi si je peux d'aider "+user,labelParole,nameAssistant)
                   else :
                       speak("J'espere que mon uttilisation te sois utile "+user,labelParole,nameAssistant)
#Menu
ryleyMenu = Menu(screen,bg="white",fg="black")
fichierMenu = Menu(ryleyMenu,tearoff=0)
appMenu = Menu(ryleyMenu,tearoff=0)
fichierMenu.add_command(label="Paramétre",command=Setting)
fichierMenu.add_command(label="Test Internet",command=TestInternet)
appMenu.add_command(label="Calculatrice",command=Calcule)
ryleyMenu.add_cascade(label="Fichier",menu=fichierMenu)
ryleyMenu.add_cascade(label="Fonction",menu=appMenu)
ryleyMenu.add_command(label="A propos",command=APropos)
screen.config(menu=ryleyMenu)
#Code principal
Introduction()
barreR = Entry(bottom,width=35,font=("arial","15"),relief=SOLID)
def micro():
    takeCommand(barreR)
def envoi():
    requete=str(barreR.get())
    varRyley = Main(requete,screen,user,labelParole,nameAssistant)
    if varRyley == 1 :
        phraseAttent()
    else :
        varRyley = search(requete,screen,user,labelParole,nameAssistant)
        if varRyley == 1 :
            phraseAttent()
        else :
            speak("Je peux pas répondre a ta requette "+user,labelParole,nameAssistant)
   
boutonEnvoyer=Button(bottom,text="Envoyer",command=envoi,bg=secondColor,fg=secondTextColor,font=("arial","15"))
boutonMicro = Button(bottom,image=imgMicro,command=micro)
#Affichage
labelParole.place(x="10",y="300")
barreR.place(x="5",y="70")
boutonEnvoyer.place(x="400",y="65")
boutonMicro.place(x="25",y="115")
#Fin de la boucle
screen.mainloop()