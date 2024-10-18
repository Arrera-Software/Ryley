from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingBETA:
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str,linux:bool):
        # variable
        self.__configFile = config
        # cadre
        self.__mainFrame = cadre
        if (linux == True):
            self.__acceuilFrame = Frame(self.__mainFrame, bg=color, width=350, height=565)
            self.__tokenGithub = Frame(self.__mainFrame, bg=color, width=350, height=565)
            self.__workFolder = Frame(self.__mainFrame, bg=color, width=350, height=565)
            self.__videoDownload = Frame(self.__mainFrame, bg=color, width=350, height=565)
        else:
            self.__acceuilFrame = Frame(self.__mainFrame, bg=color, width=350, height=600)
            self.__tokenGithub = Frame(self.__mainFrame, bg=color, width=350, height=600)
            self.__workFolder = Frame(self.__mainFrame, bg=color, width=350, height=600)
            self.__videoDownload = Frame(self.__mainFrame, bg=color, width=350, height=600)

        # Widget
        labelTitre = [
            Label(self.__acceuilFrame,text="Parametre\nde la beta",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__tokenGithub, text="Entrer votre\ntoken github", bg=color, fg=textColor, font=("arial", "20")),
            Label(self.__workFolder, text="Selectionner votre\ndossier de travail", bg=color, fg=textColor, font=("arial", "20")),
            Label(self.__videoDownload, text="Selectionner le dossier\nde telechargement des video", bg=color, fg=textColor, font=("arial", "20"))
        ]
        btnRetour = [
            Button(self.__acceuilFrame, text="Annuler", bg=color, fg=textColor, font=("arial", "15"),command=self.__backAcceuil),
            Button(self.__tokenGithub, text="Annuler", bg=color, fg=textColor, font=("arial", "15"),command=self.__backAcceuil),
            Button(self.__workFolder, text="Annuler", bg=color, fg=textColor, font=("arial", "15"),command=self.__backAcceuil),
            Button(self.__videoDownload, text="Annuler", bg=color, fg=textColor, font=("arial", "15"),command=self.__backAcceuil)
        ]
        btnValiderToken = Button(self.__tokenGithub,text="Valider", bg=color, fg=textColor, font=("arial", "15"))

        btnChoiseFolderWork = Button(self.__workFolder,text="Choisir le dossier\nde travail", bg=color, fg=textColor, font=("arial", "15"))
        btnChoiseFolderVideo = Button(self.__videoDownload,text="Choisir le dossier\nde telechargement", bg=color, fg=textColor, font=("arial", "15"))

    def view(self):
        self.__mainFrame.pack(side="left")
        self.__acceuilFrame.place(x=0,y=0)
        self.__backAcceuil()
        return True

    def __backAcceuil(self):
        self.__tokenGithub.place_forget()
        self.__workFolder.place_forget()
        self.__videoDownload.place_forget()
        self.__acceuilFrame.place(x=0,y=0)

    def __viewTokenGithub(self):
        self.__tokenGithub.place(x=0, y=0)
        self.__workFolder.place_forget()
        self.__videoDownload.place_forget()
        self.__acceuilFrame.place_forget()
