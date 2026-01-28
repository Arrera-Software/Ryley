import signal
import requests
from setting_gui.arrera_gazelle import arrera_gazelle
import time
from tkinter.messagebox import *
from lib.arrera_tk import *
import threading as th
from brain.brain import ABrain
import random
from src.ryley_widget import*

class ryley_gui(aTk):
    def __init__(self,iconFolder:str,iconName:str,
                 brain:ABrain,theme_file:str,
                 version:str):

        # Var
        self.__nameSoft = "Arrera Ryley"
        self.__first_boot = False
        self.__L_img_boot_gui = []
        self.__dir_gui_dark = "asset/GUI/dark/"
        self.__dir_gui_light = "asset/GUI/light/"

        super().__init__(title=self.__nameSoft,resizable=False,theme_file=theme_file,
                         fg_color=("#ffffff","#000000"))
        self.geometry("500x400+5+30")

        # Canvas
        self._c_boot = self.__canvas_boot()

    def active(self,firstBoot:bool,update_available:bool):

        self.__first_boot = firstBoot

        # TODO : A metre en place plus tart
        """ 
        if update_available:
            self.__c_maj.place(x=0,y=0)
        else :
            self.__boot()
        """
        self.__boot()

        self.mainloop()

    def __boot(self):
        self.__sequence_boot()



    # Creation des widget

    def __canvas_boot(self):
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b0.png",self.__dir_gui_dark+"b0.png"))
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b1.png",self.__dir_gui_dark+"b1.png"))
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b2.png",self.__dir_gui_dark+"b2.png"))
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b3.png",self.__dir_gui_dark+"b3.png"))
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b4.png",self.__dir_gui_dark+"b4.png"))
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b5.png",self.__dir_gui_dark+"b5.png"))

        l_img,d_img = self.__L_img_boot_gui[0]

        c = aBackgroundImage(self,background_light=l_img,background_dark=d_img,
                             fg_color=("#ffffff","#000000"),width=500,height=350)

        return c

    # Methode change IMG

    def __change_img_boot(self,index:int):
        if index < len(self.__L_img_boot_gui):
            l_img,d_img = self.__L_img_boot_gui[index]
        else :
            l_img,d_img = self.__L_img_boot_gui[0]

        self._c_boot.change_background(background_light=l_img,background_dark=d_img)
        self.update()

    # Methode des sequence

    def __sequence_boot(self):
        self.__change_img_boot(0)
        self._c_boot.place(x=0,y=0)
        time.sleep(0.2)
        self.__change_img_boot(1)
        time.sleep(0.2)
        self.__change_img_boot(2)
        time.sleep(0.2)
        self.__change_img_boot(3)
        time.sleep(0.2)
        self.__change_img_boot(4)
        time.sleep(0.2)
        self.__change_img_boot(5)
