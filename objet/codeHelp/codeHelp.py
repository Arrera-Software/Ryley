from tkinter import*
from src.gestionRyley import *

class CCodeHelp :
    def __init__(self,screen:Tk,gestionnaireRL:gestionRL) :
        wScreen = screen
        self.gestionnaireRyley = gestionnaireRL
        #image 
        icon = PhotoImage(file="asset/codehelp/codeHelpIcon.png")
        self.mainColor = self.gestionnaireRyley.getMaincolor()
        self.mainTextColor = self.gestionnaireRyley.getMainTextcolor()
        #Modification de la fenetre 
        wScreen.title("Ryley : Codehelp")
        wScreen.iconphoto(False,icon)
        wScreen.update()
        #cadre 
        #self.frameCodehelp =Frame(wScreen,width=500,height=600)
        #Creation Canvas
        self.fondBGTopLeft = Canvas(wScreen,width=150,height=600,bg=self.mainColor, highlightthickness=0)
        BGTopLeft = PhotoImage(file=self.gestionnaireRyley.getBGTopCodeHelpLeft(),master=self.fondBGTopLeft)
        self.fondBGTopLeft.image_names = BGTopLeft
        self.fondBGTopLeft.create_image(0,0,image=BGTopLeft,anchor="nw")
               
        self.fondBGTopRight = Canvas(wScreen,width=350,height=400,bg=self.mainColor, highlightthickness=0)
        BGTopRight = PhotoImage(file=self.gestionnaireRyley.getBGTopCodeHelpRight(),master=self.fondBGTopRight)
        self.fondBGTopRight.image_names = BGTopRight
        self.fondBGTopRight.create_image(0,0,image=BGTopRight,anchor="nw")
        
        self.fondBGBottom = Canvas(wScreen,width=350,height=200,bg=self.mainColor, highlightthickness=0)
        BGBottom = PhotoImage(file=self.gestionnaireRyley.getBGBottomCodeHelp(),master=self.fondBGBottom)
        self.fondBGBottom.image_names = BGBottom
        self.fondBGBottom.create_image(0,0,image=BGBottom,anchor="nw")
        
    def view(self):
        self.fondBGTopLeft.place(x=0,y=0)
        self.fondBGTopRight.place(x=150,y=0)
        self.fondBGBottom.place(x=150,y=400)
    
    def unView(self):
        self.fondBGTopLeft.place_forget()
        self.fondBGTopRight.place_forget()
        self.fondBGBottom.place_forget()