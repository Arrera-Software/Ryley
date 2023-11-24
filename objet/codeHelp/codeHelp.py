from tkinter import*
from tkinter import colorchooser
from src.gestionRyley import *

class CCodeHelp :
    def __init__(self,screen:Tk,gestionnaireRL:gestionRL) :
        self.__wScreen = screen
        self.__gestionnaireRyley = gestionnaireRL
        #image 
        self.__icon = PhotoImage(file="asset/codehelp/codeHelpIcon.png")
        #Creation Canvas
        #fondBGTopLeft
        self.__fondBGTopLeft = Canvas(self.__wScreen,width=150,height=600, highlightthickness=0)
        #fondBGTopRight
        self.__fondBGTopRight = Canvas(self.__wScreen,width=350,height=400, highlightthickness=0)
        #fondBGBottom
        self.__fondBGBottom = Canvas(self.__wScreen,width=350,height=200, highlightthickness=0)
        #Frame parametre
        self.__framePara = Frame(self.__wScreen,width=500,height=600)
        #widget parametre
        self.__labelPara = Label(self.__framePara,text="Parametre CodeHelp",font=("arial","15"))
        self.__btnQuitterPara = Button(self.__framePara,text="Quitter",font=("arial","15"),command=self.unViewPara)
        # BTN App sur Canvas fondBGTopLeft
        self.__btnBack = Button(self.__fondBGTopLeft,command=self.backRyley)
        self.__btnColorSelector = Button(self.__fondBGTopLeft,command=lambda:self.__selecteurColor.bootSelecteur())
        self.__btnEditeurDoc = Button(self.__fondBGTopLeft)
        self.__btnGithub = Button(self.__fondBGTopLeft)
        self.__btnLibrairy = Button(self.__fondBGTopLeft)
        self.__btnOrgaVar = Button(self.__fondBGTopLeft) 
    
    def __affichage(self):
        self.setTheme()
        self.__largeurFondAPP = self.__fondBGTopLeft.winfo_reqwidth()
        self.__btnEditeurDoc.place(x=((self.__largeurFondAPP-self.__btnEditeurDoc.winfo_reqwidth())//2),y=100)
        self.__btnGithub.place(x=((self.__largeurFondAPP-self.__btnGithub.winfo_reqwidth())//2),y=170)
        self.__btnLibrairy.place(x=((self.__largeurFondAPP-self.__btnLibrairy.winfo_reqwidth())//2),y=240)
        self.__btnOrgaVar.place(x=((self.__largeurFondAPP-self.__btnOrgaVar.winfo_reqwidth())//2),y=310)
        self.__btnColorSelector.place(x=((self.__largeurFondAPP-self.__btnColorSelector.winfo_reqwidth())//2),y=380)
        self.__btnBack.place(x=((self.__largeurFondAPP-self.__btnBack.winfo_reqwidth())//2),y=(self.__fondBGTopLeft.winfo_reqheight()-self.__btnBack.winfo_reqheight()-20))

    def __clearView(self):
        self.__btnEditeurDoc.place_forget()
        self.__btnGithub.place_forget()
        self.__btnLibrairy.place_forget()
        self.__btnOrgaVar.place_forget()
        self.__btnColorSelector.place_forget()
        self.__btnBack.place_forget()


    def setFonctionback(self,fnc):
        self.__fncBack = fnc

    def setTheme(self):
        self.__mainColor = self.__gestionnaireRyley.getMaincolor()
        self.__mainTextColor = self.__gestionnaireRyley.getMainTextcolor()
        #objet 
        self.__selecteurColor = CCHcolorSelector(self.__mainColor,self.__mainTextColor)
        #Frame parametre
        self.__framePara.configure(bg=self.__mainColor)
        #Widget parametre
        self.__btnQuitterPara.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        self.__labelPara.configure(bg=self.__mainColor,fg=self.__mainTextColor)
        #fondBGTopLeft
        BGTopLeft = PhotoImage(file=self.__gestionnaireRyley.getBGTopCodeHelpLeft(),master=self.__fondBGTopLeft)
        self.__fondBGTopLeft.image_names = BGTopLeft
        self.__fondBGTopLeft.create_image(0,0,image=BGTopLeft,anchor="nw")
        #fondBGTopRight
        BGTopRight = PhotoImage(file=self.__gestionnaireRyley.getBGTopCodeHelpRight(),master=self.__fondBGTopRight)
        self.__fondBGTopRight.image_names = BGTopRight
        self.__fondBGTopRight.create_image(0,0,image=BGTopRight,anchor="nw")
        #fondBGBottom
        BGBottom = PhotoImage(file=self.__gestionnaireRyley.getBGBottomCodeHelp(),master=self.__fondBGBottom)
        self.__fondBGBottom.image_names = BGBottom
        self.__fondBGBottom.create_image(0,0,image=BGBottom,anchor="nw")
        # BTN App sur Canvas fondBGTopLeft
        #__btnBack
        IMGBack = PhotoImage(file=self.__gestionnaireRyley.getBTNIconBack(),master=self.__btnBack)
        self.__btnBack.image_names = IMGBack
        self.__btnBack.configure(image=IMGBack)
        #__btnColorSelector
        IMGColorSelector = PhotoImage(file=self.__gestionnaireRyley.getBTNIconColorSelector(),master=self.__btnColorSelector)
        self.__btnColorSelector.image_names = IMGColorSelector
        self.__btnColorSelector.configure(image=IMGColorSelector)
        #__btnEditeurDoc
        IMGEditeurDoc = PhotoImage(file=self.__gestionnaireRyley.getBTNIconEditeurDoc(),master=self.__btnEditeurDoc)
        self.__btnEditeurDoc.image_names = IMGEditeurDoc
        self.__btnEditeurDoc.configure(image=IMGEditeurDoc)#
        #__btnGithub
        IMGGithub = PhotoImage(file=self.__gestionnaireRyley.getBTNIconGitHub(),master=self.__btnGithub)
        self.__btnGithub.image_names = IMGGithub
        self.__btnGithub.configure(image=IMGGithub)#
        #__btnLibrairy
        IMGLibrairy = PhotoImage(file=self.__gestionnaireRyley.getBTNIconLibrairy(),master=self.__btnLibrairy)
        self.__btnLibrairy.image_names = IMGLibrairy
        self.__btnLibrairy.configure(image=IMGLibrairy)#
        #__btnOrgaVar
        IMGOrgaVar = PhotoImage(file=self.__gestionnaireRyley.getBTNIconOrgaVar(),master=self.__btnOrgaVar)
        self.__btnOrgaVar.image_names = IMGOrgaVar
        self.__btnOrgaVar.configure(image=IMGOrgaVar)#
        
    def viewPara(self):
        self.__wScreen.title("Codehelp : Parametre")
        self.__framePara.pack()
        self.__fondBGTopLeft.place_forget()
        self.__fondBGTopRight.place_forget()
        self.__fondBGBottom.place_forget()
    
    def unViewPara(self):
        self.__wScreen.title("Ryley : Codehelp")
        self.__framePara.pack_forget()
        self.__clearView()
        self.__affichage()
        self.__fondBGTopLeft.place(x=0,y=0)
        self.__fondBGTopRight.place(x=150,y=0)
        self.__fondBGBottom.place(x=150,y=400)

    def view(self):
        #Modification de la fenetre 
        self.__wScreen.title("Ryley : Codehelp")
        self.__wScreen.iconphoto(False,self.__icon)
        self.__wScreen.update()
        self.__clearView()
        self.__affichage()
        self.__fondBGTopLeft.place(x=0,y=0)
        self.__fondBGTopRight.place(x=150,y=0)
        self.__fondBGBottom.place(x=150,y=400)
        #Calcule frame para
        lageurFrame = self.__framePara.winfo_reqwidth()
        hauteurFrame = self.__framePara.winfo_reqheight()
        self.__btnQuitterPara.place(x=((lageurFrame-self.__btnQuitterPara.winfo_reqwidth())//2),y=(hauteurFrame-self.__btnQuitterPara.winfo_reqheight()))
        self.__labelPara.place(x=((lageurFrame-self.__labelPara.winfo_reqwidth())//2),y=0)
    
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