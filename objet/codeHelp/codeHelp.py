from tkinter import*
from src.gestionRyley import *

class CCodeHelp :
    def __init__(self,screen:Tk,gestionnaireRL:gestionRL) :
        wScreen = screen
        self.__gestionnaireRyley = gestionnaireRL
        #image 
        icon = PhotoImage(file="asset/codehelp/codeHelpIcon.png")
        self.__mainColor = self.__gestionnaireRyley.getMaincolor()
        self.__mainTextColor = self.__gestionnaireRyley.getMainTextcolor()
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

        btnColorSelector = Button(self.__fondBGTopLeft)
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