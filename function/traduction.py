from function.JSON import*
from translate import Translator
from tkinter import *

MainColor = "white"
MainTextColor = "black"
SecondColor = "#1e23d3"
SecondTextColor = "white"



def Traduction():
    langue0=lectureJSON("setting/config.json","lang0")
    langue1=lectureJSON("setting/config.json","lang1")
    langue2=lectureJSON("setting/config.json","lang2")
    ScreenTrad=Toplevel()
    ScreenTrad.title("Ryley's Trad")
    ScreenTrad.maxsize(400,400)
    ScreenTrad.minsize(400,400)
    ScreenTrad.config(bg=SecondColor)
    labelInfo=Label(ScreenTrad,text="Resultat",bg=SecondColor,fg=SecondTextColor,font=("arial","20"))
    trad=Entry(ScreenTrad,width=45)
    def L0versL1():
        mot = str(trad.get())
        translator= Translator(from_lang=langue0,to_lang=langue1)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L0versL2():
        mot = str(trad.get())
        translator= Translator(from_lang=langue0,to_lang=langue2)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L1versL0():
        mot = str(trad.get())
        translator= Translator(from_lang=langue1,to_lang=langue0)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L1versL2():
        mot = str(trad.get())
        translator= Translator(from_lang=langue1,to_lang=langue2)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L2versL0():
        mot = str(trad.get())
        translator= Translator(from_lang=langue2,to_lang=langue0)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L2versL1():
        mot = str(trad.get())
        translator= Translator(from_lang=langue2,to_lang=langue1)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    bouttonTraduction=Button(ScreenTrad,text="Traduire",bg=SecondColor,fg=SecondTextColor)
    def Mode1():
        bouttonTraduction.config(command=L0versL1)
    def Mode2():
        bouttonTraduction.config(command=L1versL0)
    def Mode3():
        bouttonTraduction.config(command=L0versL2)
    def Mode4():
        bouttonTraduction.config(command=L2versL0)
    def Mode5():
        bouttonTraduction.config(command=L1versL2)
    def Mode6():
        bouttonTraduction.config(command=L2versL1)
    
    MenuTrad = Menu(ScreenTrad,bg="white")
    Choix = Menu(MenuTrad,tearoff=0)
    Choix.add_command(label="Langue par défault vers Langue 1",command=Mode1)
    Choix.add_command(label="Langue 1 vers Langue par défault",command=Mode2)
    Choix.add_command(label="Langue par défault vers Langue 2",command=Mode3)
    Choix.add_command(label="Langue 2 vers Langue par défault",command=Mode4)
    Choix.add_command(label="Langue 1 vers Langue 2",command=Mode5)
    Choix.add_command(label="Langue 2 vers Langue 1",command=Mode6)
    MenuTrad.add_cascade(label = "Traduction",menu=Choix)
    ScreenTrad.config(menu=MenuTrad)
    labelInfo.place(x="5",y="25")
    trad.place(relx=.5,rely=.5,anchor ="center")
    bouttonTraduction.pack(side="bottom")
    ScreenTrad.mainloop()
