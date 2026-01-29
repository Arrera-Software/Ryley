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
        self.__L_img_gui_load = []
        self.__dir_gui_dark = "asset/GUI/dark/"
        self.__dir_gui_light = "asset/GUI/light/"

        # Recuperation du cerveau
        self.__brain = brain
        # Recuperation gestionnaire
        self.__gestionnaire = self.__brain.getGestionnaire()
        # Recuperation librairy
        self.__objOS = self.__gestionnaire.getOSObjet()


        super().__init__(title=self.__nameSoft,resizable=False,theme_file=theme_file,
                         fg_color=("#ffffff","#000000"))
        self.geometry("500x400+5+30")

        # Canvas
        self.__c_boot = self.__canvas_boot()

        self.__c_maj = self.__canvas_maj()

        self.__c_speak = self.__canvas_speak()

        self.__c_load = self.__canvas_load()

        self.__back_widget = back_widget(self,[self.__dir_gui_light,self.__dir_gui_dark],
                                         "little.png","codehelp.png",
                                         self.__objOS,self.__send_on_assistant)

    def active(self,firstBoot:bool,update_available:bool):

        self.__first_boot = firstBoot

        if update_available:
            self.__c_maj.place(x=0,y=0)
        else :
            self.__boot()

        self.mainloop()

    def __boot(self):
        # TODO : Gerer le first boot
        self.__c_maj.place_forget()
        self.__sequence_boot()
        self.__sequence_speak(self.__brain.boot())


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

    def __canvas_maj(self):
        c = aBackgroundImage(self,background_light="asset/GUI/light/maj.png",
                             background_dark="asset/GUI/dark/maj.png",
                             fg_color=("#ffffff","#000000"),width=500,height=350)
        label_text = aLabel(c,
                            text="Ryley n'est pas dans sa version la plus recente.Pensez a le mettre a jour pour avoir les dernieres fonctionnalites et corrections de bugs.",
                            police_size=20,
                            fg_color=("#ffffff","#000000"),text_color=("#000000","#ffffff"),
                            wraplength=250, justify="left")

        btn_update = aButton(c, text="Mettre a jour", size=20,
                             command=lambda: wb.open("https://github.com/Arrera-Software/Ryley/releases"))

        btn_continuer = aButton(c, text="Me rappeler plus tart", size=20, command=self.__boot)

        label_text.place(x=190, y=40)
        btn_update.placeBottomLeft()
        btn_continuer.placeBottomRight()
        return c

    def __canvas_speak(self):
        c = aBackgroundImage(self,background_light="asset/GUI/light/parole.png",
                             background_dark="asset/GUI/dark/parole.png"
                             ,fg_color=("#ffffff","#000000"),width=500,height=350)

        self.__label_speak = aLabel(c,text="", wraplength=440,justify="left",
                                    police_size=20,corner_radius=0
                                    ,fg_color=("#ffffff","#000000"),
                                    text_color=("#000000","#ffffff"))

        self.__label_speak.place(x=10, y=80)

        return c

    def __canvas_load(self):
        self.__L_img_gui_load.append((self.__dir_gui_light + "load0.png", self.__dir_gui_dark + "load0.png"))
        self.__L_img_gui_load.append((self.__dir_gui_light + "load1.png", self.__dir_gui_dark + "load1.png"))
        self.__L_img_gui_load.append((self.__dir_gui_light + "load2.png", self.__dir_gui_dark + "load2.png"))
        self.__L_img_gui_load.append((self.__dir_gui_light + "load3.png", self.__dir_gui_dark + "load3.png"))
        self.__L_img_gui_load.append((self.__dir_gui_light + "load4.png", self.__dir_gui_dark + "load4.png"))

        l_img,d_img = self.__L_img_gui_load[0]

        c = aBackgroundImage(self,background_light=l_img,
                             background_dark=d_img
                             ,fg_color=("#ffffff","#000000"),width=500,height=350)

        return c

    # Methode change IMG

    def __change_img_boot(self,index:int):
        if index < len(self.__L_img_boot_gui):
            l_img,d_img = self.__L_img_boot_gui[index]
        else :
            l_img,d_img = self.__L_img_boot_gui[0]

        self.__c_boot.change_background(background_light=l_img, background_dark=d_img)
        self.update()

    def __change_img_load(self,index:int):
        if index < len(self.__L_img_gui_load):
            l_img,d_img = self.__L_img_boot_gui[index]
        else :
            l_img,d_img = self.__L_img_boot_gui[0]

        self.__c_boot.change_background(background_light=l_img, background_dark=d_img)
        self.update()

    # Partie envoie assistant

    def __send_on_assistant(self):
        print("Send assistant")
        self.focus()

    # Methode des sequence

    def __sequence_boot(self):
        self.__change_img_boot(0)
        self.__c_boot.place(x=0, y=0)
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
        time.sleep(0.2)

    def __sequence_speak(self,texte:str):
        self.__c_load.place_forget()
        self.__c_boot.place_forget()
        self.__c_speak.place(x=0,y=0)

        self.__label_speak.configure(text=texte)
        self.__back_widget.placeBottomCenter()

        self.update()
