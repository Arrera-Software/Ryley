from tkinter import*
from tkinter import colorchooser
from src.gestionRyley import *

class CCodeHelp :
    def __init__(self,screen:Tk,gestionnaireRL:gestionRL) :
        wScreen = screen
        self.__gestionnaireRyley = gestionnaireRL
        #image 
        icon = PhotoImage(file="asset/codehelp/codeHelpIcon.png")
        self.__mainColor = self.__gestionnaireRyley.getMaincolor()
        self.__mainTextColor = self.__gestionnaireRyley.getMainTextcolor()
        #objet 
        selecteurColor = CCHcolorSelector(self.__mainColor,self.__mainTextColor)
        #Modification de la fenetre 
        wScreen.title("Ryley : Codehelp")
        wScreen.iconphoto(False,icon)
        wScreen.update()
        #Creation Canvas
        #fondBGTopLeft
        self.__fondBGTopLeft = Canvas(wScreen,width=150,height=600,bg=self.__mainColor, highlightthickness=0)
        BGTopLeft = PhotoImage(file=self.__gestionnaireRyley.getBGTopCodeHelpLeft(),master=self.__fondBGTopLeft)
        self.__fondBGTopLeft.image_names = BGTopLeft
        self.__fondBGTopLeft.create_image(0,0,image=BGTopLeft,anchor="nw")
        #fondBGTopRight
        self.__fondBGTopRight = Canvas(wScreen,width=350,height=400,bg=self.__mainColor, highlightthickness=0)
        BGTopRight = PhotoImage(file=self.__gestionnaireRyley.getBGTopCodeHelpRight(),master=self.__fondBGTopRight)
        self.__fondBGTopRight.image_names = BGTopRight
        self.__fondBGTopRight.create_image(0,0,image=BGTopRight,anchor="nw")
        #fondBGBottom
        self.__fondBGBottom = Canvas(wScreen,width=350,height=200,bg=self.__mainColor, highlightthickness=0)
        BGBottom = PhotoImage(file=self.__gestionnaireRyley.getBGBottomCodeHelp(),master=self.__fondBGBottom)
        self.__fondBGBottom.image_names = BGBottom
        self.__fondBGBottom.create_image(0,0,image=BGBottom,anchor="nw")
        # BTN App sur Canvas fondBGTopLeft
        btnBack = Button(self.__fondBGTopLeft,command=self.backRyley)
        IMGBack = PhotoImage(file=self.__gestionnaireRyley.getBTNIconBack(),master=btnBack)
        btnBack.image_names = IMGBack
        btnBack.configure(image=IMGBack)

        btnColorSelector = Button(self.__fondBGTopLeft,command=lambda:selecteurColor.bootSelecteur())
        IMGColorSelector = PhotoImage(file=self.__gestionnaireRyley.getBTNIconColorSelector(),master=btnColorSelector)
        btnColorSelector.image_names = IMGColorSelector
        btnColorSelector.configure(image=IMGColorSelector)

        btnEditeurDoc = Button(self.__fondBGTopLeft)
        IMGEditeurDoc = PhotoImage(file=self.__gestionnaireRyley.getBTNIconEditeurDoc(),master=btnEditeurDoc)
        btnEditeurDoc.image_names = IMGEditeurDoc
        btnEditeurDoc.configure(image=IMGEditeurDoc)#

        btnGithub = Button(self.__fondBGTopLeft)
        IMGGithub = PhotoImage(file=self.__gestionnaireRyley.getBTNIconGitHub(),master=btnGithub)
        btnGithub.image_names = IMGGithub
        btnGithub.configure(image=IMGGithub)#

        btnLibrairy = Button(self.__fondBGTopLeft)
        IMGLibrairy = PhotoImage(file=self.__gestionnaireRyley.getBTNIconLibrairy(),master=btnLibrairy)
        btnLibrairy.image_names = IMGLibrairy
        btnLibrairy.configure(image=IMGLibrairy)#

        btnOrgaVar = Button(self.__fondBGTopLeft)
        IMGOrgaVar = PhotoImage(file=self.__gestionnaireRyley.getBTNIconOrgaVar(),master=btnOrgaVar)
        btnOrgaVar.image_names = IMGOrgaVar
        btnOrgaVar.configure(image=IMGOrgaVar)#

        #Affichage BTN 
        largeurFondAPP = self.__fondBGTopLeft.winfo_reqwidth()
        btnEditeurDoc.place(x=((largeurFondAPP-btnEditeurDoc.winfo_reqwidth())//2),y=100)
        btnGithub.place(x=((largeurFondAPP-btnGithub.winfo_reqwidth())//2),y=170)
        btnLibrairy.place(x=((largeurFondAPP-btnLibrairy.winfo_reqwidth())//2),y=240)
        btnOrgaVar.place(x=((largeurFondAPP-btnOrgaVar.winfo_reqwidth())//2),y=310)
        btnColorSelector.place(x=((largeurFondAPP-btnColorSelector.winfo_reqwidth())//2),y=380)
        btnBack.place(x=((largeurFondAPP-btnBack.winfo_reqwidth())//2),y=(self.__fondBGTopLeft.winfo_reqheight()-btnBack.winfo_reqheight()-20))

    def setFonctionback(self,fnc):
        self.__fncBack = fnc

    def view(self):
        self.__fondBGTopLeft.place(x=0,y=0)
        self.__fondBGTopRight.place(x=150,y=0)
        self.__fondBGBottom.place(x=150,y=400)
    
    def backRyley(self):
        self.__fncBack()

    def unView(self):
        self.__fondBGTopLeft.place_forget()
        self.__fondBGTopRight.place_forget()
        self.__fondBGBottom.place_forget()

    
class CCHcolorSelector:
    def __init__(self,mainColor:str,textColor:str):
        self.__mainColor = mainColor
        self.__mainTextColor = textColor

    def bootSelecteur(self):
        self.__screenColor = Toplevel()
        self.__screenColor.title("CodeHelp : selecteur de couleur")
        self.__screenColor.config(bg=self.__mainColor)
        self.__screenColor.iconphoto(False,PhotoImage(file="asset/codehelp/codeHelpIcon.png"))
        self.__screenColor.maxsize(800,500)
        self.__screenColor.minsize(800,500)
        #fonction
        #cadre
        cadreNoir = Frame(self.__screenColor,bg="black",width=325,height=325,border=100)
        self.__cadreColor = Frame(cadreNoir,bg="#ffffff",width=310,height=310)
        #label
        self.__labelIndicationCode = Label(self.__screenColor,text="Code HTML : #ffffff \nCode RGB : (255,255,255)",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15),justify="left")     
        #declaration des bouton
        buttonSelection = Button(self.__screenColor,text="Selectionner la couleur",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15),command=self.__selecteur)
        self.__buttonCopiHTLM = Button(self.__screenColor,text="Copier le code HTML",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15))
        self.__buttonCopiRGB = Button(self.__screenColor,text="Copier le code RGB",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15))
        #affichage
        self.__cadreColor.place(relx=0.5, rely=0.5, anchor=CENTER)
        cadreNoir.pack(side="right")
        self.__labelIndicationCode.place(x=15,y=15)
        buttonSelection.place(x=15,y=135)
        self.__buttonCopiHTLM.place(x=15,y=235)
        self.__buttonCopiRGB.place(x=15,y=335)
        
    def __selecteur(self):
        self.__color = colorchooser.askcolor(title="Ryley : CodeHelp selecteur de couleur",color=self.__mainColor)
        self.__colorHTLM = str(self.__color[1])
        self.__colorRGB = str(self.__color[0])
        self.__cadreColor.config(bg=self.__colorHTLM)
        self.__buttonCopiHTLM.config(command=self.__copieHTLM)
        self.__buttonCopiRGB.config(command=self.__copieRGB)
        self.__labelIndicationCode.config(text="Code HTML : "+self.__colorHTLM+"\nCode RGB : "+self.__colorRGB)
    
    def __copieHTLM(self):
        self.__screenColor.clipboard_clear()
        self.__screenColor.clipboard_append(self.__colorHTLM)
    
    def __copieRGB(self):
        self.__screenColor.clipboard_clear()
        self.__screenColor.clipboard_append(self.__colorRGB)