from tkinter import*

from openpyxl.styles.builtins import comma

from librairy.travailJSON import*
from tkinter import messagebox
from tkinter import filedialog

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
            Label(self.__acceuilFrame,text="Parametre de la beta",bg=color,fg=textColor,font=("arial","20")),
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
        btnValiderToken = Button(self.__tokenGithub,text="Valider", bg=color, fg=textColor, font=("arial", "15"),command=self.__setTokenGithub)

        btnChoiseFolderWork = Button(self.__workFolder,text="Choisir le dossier\nde travail",
                                     bg=color, fg=textColor, font=("arial", "15"),command=self.__setFolderWork)
        btnChoiseFolderVideo = Button(self.__videoDownload,text="Choisir le dossier\nde telechargement",
                                      bg=color, fg=textColor, font=("arial", "15"),command=self.__setFolderDownload)

        # Varriable
        centrageAcceuil = self.__acceuilFrame.winfo_reqwidth()

        # Bouton Acceuil
        btnToken = Button(self.__acceuilFrame,text="Enregistrement du\ntoken github", bg=color,
                          fg=textColor, font=("arial", "15"),command= self.__viewTokenGithub)
        btnWord = Button(self.__acceuilFrame,text="Parametre Arrera Work", bg=color,
                         fg=textColor, font=("arial", "15"),command= self.__viewTokenWork)
        btnVideo = Button(self.__acceuilFrame,text="Parametre Arrera\nvideo download", bg=color,
                          fg=textColor, font=("arial", "15"),command= self.__viewTokenVideo)

        self.__entryToken = Entry(self.__tokenGithub, font=("arial", "15"), borderwidth=2, relief="solid")

        # Affichage
        labelTitre[0].place(relx=0.5, rely=0.0, anchor="n")
        labelTitre[1].place(relx=0.5, rely=0.0, anchor="n")
        labelTitre[2].place(relx=0.5, rely=0.0, anchor="n")
        labelTitre[3].place(relx=0.5, rely=0.0, anchor="n")

        btnToken.place(x=((centrageAcceuil - btnToken.winfo_reqwidth()) // 2), y=150)
        btnWord.place(x=((centrageAcceuil-btnWord.winfo_reqwidth())//2),y=250)
        btnVideo.place(x=((centrageAcceuil - btnVideo.winfo_reqwidth()) // 2), y=350)

        btnRetour[0].place(relx=0, rely=1, anchor='sw')
        btnRetour[1].place(relx=0, rely=1, anchor='sw')
        btnRetour[2].place(relx=0, rely=1, anchor='sw')
        btnRetour[3].place(relx=0, rely=1, anchor='sw')

        btnChoiseFolderWork.place(relx=0.5, rely=0.5, anchor="center")
        btnChoiseFolderVideo.place(relx=0.5, rely=0.5, anchor="center")

        btnValiderToken.place(relx=1, rely=1, anchor='se')

        self.__entryToken.place(relx=0.5, rely=0.5, anchor="center")

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

    def __viewTokenWork(self):
        self.__tokenGithub.place_forget()
        self.__workFolder.place(x=0, y=0)
        self.__videoDownload.place_forget()
        self.__acceuilFrame.place_forget()

    def __viewTokenVideo(self):
        self.__tokenGithub.place_forget()
        self.__workFolder.place_forget()
        self.__videoDownload.place(x=0, y=0)
        self.__acceuilFrame.place_forget()

    def __setFolderWork(self):
        workFolder = filedialog.askdirectory(title="Choix dossier de travail Arrera Work")
        if workFolder :
            self.__configFile.EcritureJSON("wordFolder",workFolder)
            messagebox.showinfo("Arrera Work","Votre dossier a été bien enregistrée")
        else :
            messagebox.showerror("Arrera Work","Impossible d'enregistrer le dossier")
        self.__backAcceuil()

    def __setFolderDownload(self):
        downloadFolder = filedialog.askdirectory(title="Choix dossier de telechargement")
        if downloadFolder :
            self.__configFile.EcritureJSON("videoDownloadFolder",downloadFolder)
            messagebox.showinfo("Arrera Video Download","Votre dossier a été bien enregistrée")
        else :
            messagebox.showerror("Arrera Video Download","Impossible d'enregistrer le dossier")
        self.__backAcceuil()

    def __setTokenGithub(self):
        token = self.__entryToken.get()
        if token:
            self.__configFile.EcritureJSON("tokenGithub",token)
            messagebox.showinfo("Token github","Enregistrement du token")
            self.__entryToken.delete(0,END)
        else :
            messagebox.showerror("Token githib","Impossible d'enregistrer un token null")
        self.__backAcceuil()