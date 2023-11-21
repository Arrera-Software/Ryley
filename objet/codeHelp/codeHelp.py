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
        #cadre 
        #self.frameCodehelp =Frame(wScreen,width=500,height=600)
        #Creation Canvas
        self.__fondBGTopLeft = Canvas(wScreen,width=150,height=600,bg=self.__mainColor, highlightthickness=0)
        BGTopLeft = PhotoImage(file=self.__gestionnaireRyley.getBGTopCodeHelpLeft(),master=self.__fondBGTopLeft)
        self.__fondBGTopLeft.image_names = BGTopLeft
        self.__fondBGTopLeft.create_image(0,0,image=BGTopLeft,anchor="nw")
               
        self.__fondBGTopRight = Canvas(wScreen,width=350,height=400,bg=self.__mainColor, highlightthickness=0)
        BGTopRight = PhotoImage(file=self.__gestionnaireRyley.getBGTopCodeHelpRight(),master=self.__fondBGTopRight)
        self.__fondBGTopRight.image_names = BGTopRight
        self.__fondBGTopRight.create_image(0,0,image=BGTopRight,anchor="nw")
        
        self.__fondBGBottom = Canvas(wScreen,width=350,height=200,bg=self.__mainColor, highlightthickness=0)
        BGBottom = PhotoImage(file=self.__gestionnaireRyley.getBGBottomCodeHelp(),master=self.__fondBGBottom)
        self.__fondBGBottom.image_names = BGBottom
        self.__fondBGBottom.create_image(0,0,image=BGBottom,anchor="nw")
        
    def view(self):
        self.__fondBGTopLeft.place(x=0,y=0)
        self.__fondBGTopRight.place(x=150,y=0)
        self.__fondBGBottom.place(x=150,y=400)
    
    def unView(self):
        self.__fondBGTopLeft.place_forget()
        self.__fondBGTopRight.place_forget()
        self.__fondBGBottom.place_forget()