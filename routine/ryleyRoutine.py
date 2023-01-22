from src.varriable import*
from tkinter import*
from function.JSON import*

class ryleyRoutine :
    def __init__(self):
        self.routine = Tk()
        #self.routine = Toplevel()
        self.routine.title("Ryley : Routine")
        self.routine.maxsize(500,500)
        self.routine.minsize(500,500)
        self.routine.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        self.routine.config(bg=mainColor)
        #var
        self.syntaxeRoutine = {"name":"","boot":"","fnc":""}
        self.listFnc = ["Ouvrir un logiciel","Ouvrir une page web","Dire la meteo","Dire les actualiter","Dire une phrase"]
        self.listBoot = ["Demarage manuel","Demarage a une heure presise"]
        self.varFnc = StringVar(self.routine)
        self.varBoot = StringVar(self.routine)
        #image
        self.imageCree = PhotoImage(file="image/routine/creeRoutine.png")
        self.imageList = PhotoImage(file="image/routine/listRoutine.png")
        self.imageTrash = PhotoImage(file="image/routine/routineTrash.png")
        self.imageValider = PhotoImage(file="image/routine/validerRoutine.png")
        self.imageQuit = PhotoImage(file="image/routine/routineQuit.png")
        #cadre
        self.frameMain = Frame(self.routine,width=500,height=425,bg=mainColor)
        self.frameEcriture = Frame(self.routine,width=500,height=425,bg=mainColor)
        self.frameListe = Frame(self.routine,width=500,height=425,bg=mainColor)
        #Label
        self.labelText = Label(self.routine,bg=mainColor,fg=mainTextColor,font=("arial",20))
        self.labelIndicationNom = Label(self.frameEcriture,bg=mainColor,fg=mainTextColor,text="Nom :",font=("arial",15))
        self.labelIndicationBoot = Label(self.frameEcriture,bg=mainColor,fg=mainTextColor,text="Condition de demarage : ",font=("arial",15))
        self.labelIndicationfnc = Label(self.frameEcriture,bg=mainColor,fg=mainTextColor,text="Fonction de la routine : ",font=("arial",15))
        self.labelListRoutine= Label(self.frameListe,bg=mainColor,fg=mainTextColor,font=("arial",15),text="aaa",justify="center")
        #bouton
        self.btnCreate = Button(self.frameMain,image=self.imageCree,bg=mainColor,fg=mainTextColor,command=self.NewRoutine)
        self.btnList = Button(self.frameMain,image=self.imageList,bg=mainColor,fg=mainTextColor,command=self.ListeShow)
        self.btnTrash = Button(self.frameMain,image=self.imageTrash,bg=mainColor,fg=mainTextColor)
        self.btnValiderEcriture = Button(self.frameEcriture,image=self.imageValider,bg=mainColor,fg=mainTextColor)
        self.btnQuitEcriture = Button(self.frameEcriture,image=self.imageQuit,bg=mainColor,fg=mainTextColor)
        self.btnValiderListe = Button(self.frameListe,image=self.imageValider,bg=mainColor,fg=mainTextColor)
        self.btnQuitListe = Button(self.frameListe,image=self.imageQuit,bg=mainColor,fg=mainTextColor)
        #menu a  Option
        self.menuBoot = OptionMenu(self.frameEcriture,self.varBoot,*self.listBoot)
        self.menuFnc = OptionMenu(self.frameEcriture,self.varFnc,*self.listFnc) 
        #entry
        self.entryNameRoutine = Entry(self.frameEcriture,width=15,font=("arial","15"),relief=SOLID)
        self.entryListeRoutine = Entry(self.frameListe,width=10,font=("arial","15"),relief=SOLID,justify="center")
        #affichage
        self.MainShow()
        self.labelText.pack()
        self.routine.mainloop()
    
    def MainShow(self):
        self.labelText.config(text="Routine")
        self.frameMain.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.btnCreate.place(x=125,y=15)
        self.btnTrash.place(x=125,y=145)
        self.btnList.place(x=125,y=270)
        
    def MainNoShow(self):
        self.frameMain.place_forget()
        self.btnCreate.place_forget()
        self.btnList.place_forget()
    
    def EcritureShow(self):
        self.labelText.config(text="Cree vos routine")
        self.frameEcriture.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.btnValiderEcriture.place(x=420,y=345)
        self.btnQuitEcriture.place(x=0,y=345)
        self.labelIndicationNom.place(x=0,y=30)
        self.labelIndicationBoot.place(x=0,y=90)
        self.labelIndicationfnc.place(x=0,y=150)
        self.entryNameRoutine.place(x=60,y=30)
        self.menuBoot.place(x=250,y=90)
        self.menuFnc.place(x=250,y=150)
    
    def EcritureNoShow(self):
        self.frameEcriture.place_forget()
        self.btnValiderEcriture.place_forget()
        self.btnQuitEcriture.place_forget()
        self.labelIndicationNom.place_forget()
        self.labelIndicationBoot.place_forget()
        self.labelIndicationfnc.place_forget()
        self.entryNameRoutine.place_forget()
        self.menuBoot.place_forget()
        self.menuFnc.place_forget()
    
    def NewRoutine(self):
        def creationRoutine():
            routineNb = str(compteurJSON("routine/routine.json")+1)
            newRoutine = self.syntaxeRoutine
            newRoutine["name"] = str(self.entryNameRoutine.get())
            newRoutine["boot"] = str(self.varBoot.get())
            newRoutine["fnc"] = str(self.varFnc.get())
            EcritureSansEcrasement("routine/routine.json",newRoutine,routineNb)
            self.EcritureNoShow()
            self.MainShow()
        def Quit():
            self.EcritureNoShow()
            self.MainShow()
        self.btnQuitEcriture.config(command=Quit)
        self.btnValiderEcriture.config(comman=creationRoutine)
        self.EcritureShow()
        self.MainNoShow()
    
    def ListeShow(self):
        self.MainNoShow()
        def Quit():
            self.ListeNoShow()
            self.MainShow()
        def valider():
            routine=self.entryListeRoutine.get()
            self.entryListeRoutine.place_forget()
            self.btnValiderListe.place_forget()
            self.btnQuitListe.place(x=210,y=345)
            self.labelListRoutine.config(justify="left",text="Nom: "+str(lectureSimpleJSON("routine/routine.json")["1"]["name"])+"\n\nboot: "+str(lectureSimpleJSON("routine/routine.json")["1"]["boot"])+"\n\nFonction: "+str(lectureSimpleJSON("routine/routine.json")["1"]["fnc"]))
        nbRoutine = str(compteurJSON("routine/routine.json"))
        self.labelText.config(text="liste de routine")
        self.frameListe.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.btnValiderListe.place(x=420,y=345)
        self.btnQuitListe.place(x=0,y=345)
        self.labelListRoutine.place(x=120,y=30)
        self.entryListeRoutine.place(x=180,y=90)
        self.labelListRoutine.configure(text="Il a "+nbRoutine+" enregistrer routine")
        self.btnQuitListe.config(command=Quit)
        self.btnValiderListe.config(command=valider)
        
    def ListeNoShow(self):
        self.frameListe.place_forget()
        self.btnValiderListe.place_forget()
        self.btnQuitListe.place_forget()
        self.labelListRoutine.place_forget()
        self.entryListeRoutine.place_forget()
        
            

        