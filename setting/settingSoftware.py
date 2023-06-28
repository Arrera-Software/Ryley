from tkinter import *
from function.JSON import*
from setting.view import*
from src.varriable import*
from tkinter.filedialog import askopenfilename

def Software(cadre,screen,btn1,btn2,btn3,btn4,btn5):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg=mainColor)
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5)
    def Affichage():
        labelSoft1.place(x=20,y=125)
        labelSoft2.place(x=20,y=175)
        labelSoft3.place(x=20,y=225)
        labelSoft4.place(x=20,y=275)
        labelSoft5.place(x=20,y=325)
        
        btnSoft1.place(x=195,y=125)
        btnSoft2.place(x=195,y=175)
        btnSoft3.place(x=195,y=225)
        btnSoft4.place(x=195,y=275)
        btnSoft5.place(x=195,y=325)
    def NoAffichage():
        labelSoft1.place_forget()
        labelSoft2.place_forget()
        labelSoft3.place_forget()
        labelSoft4.place_forget()
        labelSoft5.place_forget()
        
        btnSoft1.place_forget()
        btnSoft2.place_forget()
        btnSoft3.place_forget()
        btnSoft4.place_forget()
        btnSoft5.place_forget()
    
    def SoftView():
        labelSoftName.place(x=20,y=125)
        entryName.place(x=100,y=230)
        btnSoftValider.place(x=225,y=300)
    def NoSoftView():
        labelSoftName.place_forget()
        entryName.place_forget()
        btnSoftValider.place_forget()
    
    def ExitModif():
        btnSoftQuit.config(command=exit)
        Affichage()
        NoSoftView()
        
    def soft1():
        NoAffichage()
        SoftView()
        btnSoftQuit.config(command=ExitModif)
        def validerEtape():
            EcritureJSON("setting/config.json","nameSoft1",entryName.get())
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","EmplacementSoft1",var)
            ExitModif()
        btnSoftValider.config(command=validerEtape)
        
    def soft2():
        NoAffichage()
        SoftView()
        btnSoftQuit.config(command=ExitModif)
        def validerEtape():
            EcritureJSON("setting/config.json","nameSoft2",entryName.get())
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","EmplacementSoft2",var)
            ExitModif()
        btnSoftValider.config(command=validerEtape)
        
    def soft3():
        NoAffichage()
        SoftView()
        btnSoftQuit.config(command=ExitModif)
        def validerEtape():
            EcritureJSON("setting/config.json","nameSoft3",entryName.get())
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","EmplacementSoft3",var)
            ExitModif()
        btnSoftValider.config(command=validerEtape)
        
    def soft4():
        NoAffichage()
        SoftView()
        btnSoftQuit.config(command=ExitModif)
        def validerEtape():
            EcritureJSON("setting/config.json","nameSoft4",entryName.get())
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","EmplacementSoft4",var)
            ExitModif()
        btnSoftValider.config(command=validerEtape)
        
    def soft5():
        NoAffichage()
        SoftView()
        btnSoftQuit.config(command=ExitModif)
        def validerEtape():
            EcritureJSON("setting/config.json","nameSoft5",entryName.get())
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","EmplacementSoft5",var)
            ExitModif()
        btnSoftValider.config(command=validerEtape)
    
    #declaration widget
    #btn
    btnSoft1 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=soft1)
    btnSoft2 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=soft2)
    btnSoft3 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=soft3)
    btnSoft4 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=soft4)
    btnSoft5 = Button(section,text="Modifier",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=soft5)
    btnSoftQuit = Button(section,text="Exit",bg=secondColor,font=("arial","15"),fg=secondTextColor,command=exit)
    btnSoftValider = Button(section,text="Valider",bg=secondColor,font=("arial","15"),fg=secondTextColor)
    #Label
    labelIndication =Label(section,text="Changer la localisation \nde vos lieu",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelSoft1 = Label(section,text="Logiciel 1",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelSoft2 = Label(section,text="Logiciel 2",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelSoft3 = Label(section,text="Logiciel 3",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelSoft4 = Label(section,text="Logiciel 4",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    labelSoft5 = Label(section,text="Logiciel 5",bg=mainColor,font=("arial","15"),fg=mainTextColor)
    
    labelSoftName = Label(section,text="Nom :",bg=mainColor,font=("arial","15"),fg=mainTextColor) 
    #entry
    entryName = Entry(section,width=30,font=("arial","15"),relief=SOLID)
    
    labelIndication.place(x=125,y=0)
    
    Affichage()
    
    btnSoftQuit.place(x=225,y=625)