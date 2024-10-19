from tkinter import*
from librairy.travailJSON import *
from librairy.dectectionOS import *
import webbrowser as wb

class CArreraReturnToolKit :
    def __init__(self,debugConf:str):
        configFile = jsonWork(debugConf)
        self.__name = configFile.lectureJSON("NameSoft")
        self.__color = configFile.lectureJSON("color")
        self.__textcolor = configFile.lectureJSON("textColor")
        self.__styleTextTitle = ("Arial",25)
        self.__styleText = ("Arial", 15)
        self.__txtBTN = [configFile.lectureJSON("btn1Text"),configFile.lectureJSON("btn3Text"),
                         configFile.lectureJSON("btn2Text"),configFile.lectureJSON("btn4Text")]
        self.__linkBTN = [configFile.lectureJSON("btn1Link"),configFile.lectureJSON("btn3Link"),
                         configFile.lectureJSON("btn2Link"),configFile.lectureJSON("btn4Link")]

    def active(self):
        # Creation de la fenetre
        win = Toplevel()
        win.title(self.__name)
        if (OS().osLinux() == True):
            win.maxsize(500, 635)
            win.minsize(500, 635)
        else:
            win.maxsize(500, 610)
            win.minsize(500, 610)
        win.configure(bg=self.__color)
        # Frame
        frameBTN = Frame(win,width=400,height=400,bg=self.__color)
        # Widget
        # Win
        labelTitle = Label(win,text=self.__name,
                           bg=self.__color,
                           font=self.__styleTextTitle,fg=self.__textcolor)
        btnQuit = Button(win,text="Quitter",bg=self.__color,
                         fg=self.__textcolor,font=self.__styleText,
                         command=lambda : win.quit())
        #BTN
        btn1 = Button(frameBTN,text=self.__txtBTN[0],font=self.__styleText,
                      bg=self.__color,fg=self.__textcolor,wraplength=100,
                      command= lambda : wb.open(self.__linkBTN[0]))
        btn2 = Button(frameBTN, text=self.__txtBTN[1], font=self.__styleText,
                      bg=self.__color, fg=self.__textcolor,wraplength=100,
                      command= lambda : wb.open(self.__linkBTN[1]))
        btn3 = Button(frameBTN, text=self.__txtBTN[2], font=self.__styleText,
                      bg=self.__color, fg=self.__textcolor,wraplength=120,
                      command= lambda : wb.open(self.__linkBTN[2]))
        btn4 = Button(frameBTN, text=self.__txtBTN[3], font=self.__styleText,
                      bg=self.__color, fg=self.__textcolor,wraplength=100,
                      command= lambda : wb.open(self.__linkBTN[3]))
        # Affichage
        frameBTN.place(relx=0.5, rely=0.5, anchor="center")

        if self.__txtBTN[0] and self.__linkBTN[0] :
            btn1.place(relx=0.0, rely=0.0, anchor='nw')
        if self.__txtBTN[1] and self.__linkBTN[1]:
            btn2.place(relx=1.0, rely=0.0, anchor='ne')
        if self.__txtBTN[2] and self.__linkBTN[2]:
            btn3.place(relx=0, rely=1, anchor='sw')
        if self.__txtBTN[3] and self.__linkBTN[3]:
            btn4.place(relx=1, rely=1, anchor='se')

        labelTitle.pack()
        btnQuit.pack(side="bottom")