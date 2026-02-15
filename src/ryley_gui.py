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
from src.ryley_language import ryley_language

class ryley_gui(aTk):
    def __init__(self,iconFolder:str,iconName:str,
                 brain:ABrain,theme_file:str,
                 version:str):

        # Var
        self.__nameSoft = "Arrera Ryley"
        self.__first_boot = False
        self.__assistant_load = False
        self.__setting_is_enabled = False
        self.__little_enabled = False
        self.__timer = 0
        self.__L_img_boot_gui = []
        self.__L_img_gui_load = []
        self.__L_img_emotion = []
        self.__L_img_emotion_little = []
        self.__L_img_load_little = []
        self.__dir_gui_dark = "asset/GUI/dark/"
        self.__dir_gui_light = "asset/GUI/light/"
        self.__index_load = 0
        self.__version = version

        # Liste de widget
        self.__L_btn_tableur_normal = []
        self.__L_btn_word_normal = []
        self.__L_btn_project_normal = []

        # Recuperation du cerveau
        self.__brain = brain
        # Recuperation gestionnaire
        self.__gestionnaire = self.__brain.getGestionnaire()
        # Recuperation librairy
        self.__objOS = self.__gestionnaire.getOSObjet()

        # Language Ryley
        self.__language = ryley_language("json_conf/language_ryley.json")
        # Theard
        self.__th_reflect = th.Thread()

        super().__init__(title=self.__nameSoft,resizable=False,theme_file=theme_file,
                         fg_color=("#ffffff","#000000"))
        self.geometry("500x400+5+30")
        self.protocol("WM_DELETE_WINDOW", self.__on_close)

        if self.__objOS.osLinux():
            self.__emplacementIcon = iconFolder+"linux/"+iconName+".png"
            self.iconphoto(False,PhotoImage(file=self.__emplacementIcon))
        elif self.__objOS.osWindows():
            self.__emplacementIcon = iconFolder+"win/"+iconName+".ico"
            self.iconbitmap(self.__emplacementIcon)
        elif self.__objOS.osMac():
            self.__emplacementIcon = resource_path(iconFolder+"mac/"+iconName+".png")
            self.iconphoto(False,PhotoImage(file=self.__emplacementIcon))

        # Initilisation du gestionnaire de clavier
        self.__key_gest = keyboad_manager(self)

        # Init des parametre
        self.__gazelleUI = arrera_gazelle(self,self.__gestionnaire,"json_conf/conf-setting.json")
        self.__gazelleUI.passFNCQuit(self.__quit_setting)
        self.__gazelleUI.passFNCBTNIcon(self.__about)

        # Canvas
        self.__c_boot = self.__canvas_boot()

        self.__c_maj = self.__canvas_maj()

        self.__c_speak_normal = self.__canvas_speak_normal()

        self.__c_speak_little = self.__canvas_speak_little()

        self.__c_load_normal = self.__canvas_load_normal()

        self.__c_load_little = self.__canvas_load_little()

        self.__c_emotion_normal = self.__canvas_emmotion_normal()

        self.__c_emotion_little = self.__canvas_emmotion_little()

        self.__back_widget_normal = back_widget(self, self.__key_gest
                                                , [self.__dir_gui_light,self.__dir_gui_dark],
                                         "little.png",
                                         "codehelp.png",
                                                self.__objOS, self.__send_on_assistant,
                                                self.__mode_codehelp_normal,
                                                self.__mode_little, self.__active_setting)

        self.__back_widget_little = back_widget(self, self.__key_gest
                                                , [self.__dir_gui_light,self.__dir_gui_dark],
                                                "big.png",
                                                "codehelp.png",
                                                self.__objOS, self.__send_on_assistant,
                                                self.__mode_codehelp_normal,
                                                self.__mode_normal, self.__active_setting)

    def active(self,firstBoot:bool,update_available:bool):

        self.__first_boot = firstBoot

        if update_available:
            self.__c_maj.place(x=0,y=0)
        else :
            self.__boot()

        self.mainloop()

    def __boot(self):
        self.__c_maj.place_forget()
        if self.__first_boot :
            self.__sequence_first_boot()
        else :
            self.__sequence_boot()
            self.__sequence_speak(self.__brain.boot())
        self.__update__assistant()


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
                            text="Ryley n’est pas dans sa version la plus récente. Pensez à le mettre à jour pour avoir les dernières fonctionnalités et corrections de bugs.",
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

    def __canvas_speak_normal(self):
        c = aBackgroundImage(self,background_light="asset/GUI/light/parole.png",
                             background_dark="asset/GUI/dark/parole.png"
                             ,fg_color=("#ffffff","#000000"),width=500,height=350)

        self.__label_speak_normal = aLabel(c, text="", wraplength=440, justify="left",
                                           police_size=20, corner_radius=0
                                           , fg_color=("#ffffff","#000000"),
                                           text_color=("#000000","#ffffff"))

        tableurIMG = aImage(path_dark="asset/GUI/dark/tableur.png",
                            path_light="asset/GUI/light/tableur.png", width=30, height=30)
        wordIMG = aImage(path_dark="asset/GUI/dark/word.png",
                         path_light="asset/GUI/light/word.png", width=30, height=30)
        projetrIMG = aImage(path_dark="asset/GUI/dark/projet.png",
                            path_light="asset/GUI/light/projet.png", width=30, height=30)

        self.__label_speak_normal.place(x=10, y=80)

        self.__L_btn_tableur_normal.append(aButton(c, width=30, height=30, text="", image=tableurIMG,
                                                   dark_color="#1f1f1f", light_color="#e0e0e0",
                                                   hover_color=("#949494", "#505050"),
                                                   command=lambda : self.__set_requette_with_btn("aide tableur")))
        self.__L_btn_word_normal.append(aButton(c, width=30, height=30, text="", image=wordIMG,
                                                dark_color="#1f1f1f", light_color="#e0e0e0",
                                                hover_color=("#949494", "#505050"),
                                                command = lambda : self.__set_requette_with_btn("aide word")))
        self.__L_btn_project_normal.append(aButton(c, width=30, height=30, text="", image=projetrIMG,
                                                   dark_color="#1f1f1f", light_color="#e0e0e0",
                                                   hover_color=("#949494", "#505050"),
                                                   command=lambda: self.__set_requette_with_btn("aide projet")))

        return c

    def __canvas_speak_little(self):
        c = aBackgroundImage(self,background_light="asset/GUI/light/parole_little.png",
                             background_dark="asset/GUI/dark/parole_little.png"
                             ,fg_color=("#ffffff","#000000"),width=500,height=70)

        self.__label_speak_little = aLabel(c, text="", wraplength=440, justify="left",
                                           police_size=15, corner_radius=0
                                           , fg_color=("#102876","#102876"),
                                           text_color=("#ffffff","#ffffff"))

        self.__label_speak_little.place(x=12,y=15)

        return  c


    def __canvas_load_normal(self):
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

    def __canvas_load_little(self):
        self.__L_img_load_little.append((self.__dir_gui_light + "little-load0.png", self.__dir_gui_dark + "little-load0.png"))
        self.__L_img_load_little.append((self.__dir_gui_light + "little-load1.png", self.__dir_gui_dark + "little-load1.png"))
        self.__L_img_load_little.append((self.__dir_gui_light + "little-load2.png", self.__dir_gui_dark + "little-load2.png"))
        self.__L_img_load_little.append((self.__dir_gui_light + "little-load3.png", self.__dir_gui_dark + "little-load3.png"))
        self.__L_img_load_little.append((self.__dir_gui_light + "little-load4.png", self.__dir_gui_dark + "little-load4.png"))

        l_img,d_img = self.__L_img_load_little[0]

        c = aBackgroundImage(self,background_light=l_img,
                             background_dark=d_img
                             ,fg_color=("#ffffff","#000000"),width=500,height=70)

        return c

    def __canvas_emmotion_normal(self):
        self.__L_img_emotion.append((self.__dir_gui_light + "w0.png", self.__dir_gui_dark + "w0.png"))
        self.__L_img_emotion.append((self.__dir_gui_light + "w1.png", self.__dir_gui_dark + "w1.png"))
        self.__L_img_emotion.append((self.__dir_gui_light + "w2.png", self.__dir_gui_dark + "w2.png"))
        self.__L_img_emotion.append((self.__dir_gui_light + "w3.png", self.__dir_gui_dark + "w3.png"))
        self.__L_img_emotion.append((self.__dir_gui_light + "w4.png", self.__dir_gui_dark + "w4.png"))

        l_img,d_img = self.__L_img_emotion[0]
        c = aBackgroundImage(self,background_light=l_img,background_dark=d_img,width=500,height=350)

        return c

    def __canvas_emmotion_little(self):
        self.__L_img_emotion_little.append((self.__dir_gui_light + "little-w0.png", self.__dir_gui_dark + "little-w0.png"))
        self.__L_img_emotion_little.append((self.__dir_gui_light + "little-w1.png", self.__dir_gui_dark + "little-w1.png"))
        self.__L_img_emotion_little.append((self.__dir_gui_light + "little-w2.png", self.__dir_gui_dark + "little-w2.png"))
        self.__L_img_emotion_little.append((self.__dir_gui_light + "little-w3.png", self.__dir_gui_dark + "little-w3.png"))
        self.__L_img_emotion_little.append((self.__dir_gui_light + "little-w4.png", self.__dir_gui_dark + "little-w4.png"))

        l_img,d_img = self.__L_img_emotion_little[0]
        c = aBackgroundImage(self,background_light=l_img,background_dark=d_img,width=500,height=70)

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
            l_img_normal,d_img_normal = self.__L_img_gui_load[index]
            l_img_little,d_img_little = self.__L_img_load_little[index]
        else :
            l_img_normal,d_img_normal = self.__L_img_gui_load[0]
            l_img_little,d_img_little = self.__L_img_load_little[0]


        self.__c_load_normal.change_background(background_light=l_img_normal, background_dark=d_img_normal)
        self.__c_load_little.change_background(background_light=l_img_little, background_dark=d_img_little)
        self.update()

    def __change_img_emotion(self,index:int):
        if index < len(self.__L_img_emotion):
            l_img_normal,d_img_normal = self.__L_img_emotion[index]
            l_img_little,d_img_little = self.__L_img_emotion_little[index]
        else :
            l_img_normal,d_img_normal = self.__L_img_emotion[0]
            l_img_little,d_img_little = self.__L_img_emotion_little[0]

        self.__c_emotion_normal.change_background(background_light=l_img_normal, background_dark=d_img_normal)
        self.__c_emotion_little.change_background(background_light=l_img_little, background_dark=d_img_little)
        self.update()

    # Partie gestion assistant

    def __send_on_assistant(self):
        self.focus()
        if not self.__little_enabled:
            content = self.__back_widget_normal.get_text_entry()
            self.__back_widget_normal.clear_entry()
            self.__back_widget_normal.place_forget()
        else :
            content = self.__back_widget_little.get_text_entry()
            self.__back_widget_little.clear_entry()
            self.__back_widget_little.place_forget()

        if content:
            if "parametre" in content or "settings" in content:
                self.__active_setting()
            else :
                self.__th_reflect = th.Thread(target=self.__brain.neuron,args=(content,))
                self.__th_reflect.start()
                self.__update_during_assistant_reflect(True)

    def __treatment_out_assistant(self,var:int,out:list):
        if var == 15:
            self.__on_close()
        elif var == 17:
            self.__windows_help_assistant(out[0])
        else :
           self.__sequence_speak(out[0])

        self.__manage_btn_open_fnc()

    def __set_requette_with_btn(self,requette:str):
        if not self.__little_enabled:
            self.__back_widget_normal.clear_entry()
            self.__back_widget_normal.insert_text(requette)
        else :
            self.__back_widget_little.clear_entry()
            self.__back_widget_little.insert_text(requette)
        self.__send_on_assistant()


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
        for btn in self.__L_btn_tableur_normal:
            btn.place_forget()
        for btn in self.__L_btn_word_normal:
            btn.place_forget()
        for btn in self.__L_btn_project_normal:
            btn.place_forget()
        self.__timer = 0
        self.__assistant_speak = True
        self.__c_load_normal.place_forget()
        self.__c_load_little.place_forget()
        self.__c_emotion_little.place_forget()
        self.__c_emotion_normal.place_forget()
        self.__c_boot.place_forget()

        self.__back_widget_little.place_forget()
        self.__back_widget_normal.place_forget()

        if not self.__little_enabled:
            self.__c_speak_normal.place(x=0, y=0)
            self.__label_speak_normal.configure(text=texte)
            self.__back_widget_normal.placeBottomCenter()
        else :
            self.__c_speak_little.place(x=0, y=0)
            self.__label_speak_little.configure(text=texte)
            self.__back_widget_little.placeBottomCenter()


        self.__assistant_speak = False
        self.update()

    def __sequence_stop(self):
        if self.__little_enabled:
            self.geometry("500x400+5+30")
            self.update()
            self.__c_speak_little.place_forget()
            self.__c_emotion_little.place_forget()
            self.__little_enabled = False

        self.__c_emotion_normal.place_forget()
        self.__c_emotion_little.place_forget()
        self.__sequence_speak(self.__brain.shutdown())
        self.__assistant_speak = True
        self.__back_widget_normal.place_forget()
        self.__back_widget_little.placeBottomCenter()
        self.update()
        time.sleep(0.8)
        self.__c_speak_normal.place_forget()
        self.__c_load_normal.place_forget()
        self.__c_load_little.place_forget()
        self.__change_img_boot(5)
        self.__c_boot.place(x=0, y=0)
        time.sleep(0.2)
        self.__change_img_boot(4)
        time.sleep(0.2)
        self.__change_img_boot(3)
        time.sleep(0.2)
        self.__change_img_boot(2)
        time.sleep(0.2)
        self.__change_img_boot(1)
        time.sleep(0.2)
        self.__change_img_boot(0)

    def __sequence_first_boot(self):
        self.__sequence_speak(self.__language.get_first_boot(1))
        time.sleep(1.5)
        self.__sequence_speak(self.__language.get_first_boot(2))
        time.sleep(1.5)
        self.__sequence_speak(self.__brain.boot())

    def __sequence_emotion(self):
        if 10 >= self.__timer >= 40:
            self.__change_img_emotion(0)
        elif 41 <= self.__timer >= 80:
            self.__change_img_emotion(1)
        elif 81 <= self.__timer >= 120:
            self.__change_img_emotion(2)
        elif 121 <= self.__timer >= 160:
            self.__change_img_emotion(3)
        elif 161 <= self.__timer >= 200:
            self.__change_img_emotion(4)
        else :
            self.__change_img_emotion(0)


    # Methode de modification de l'interface

    def __mode_normal(self):
        self.geometry("500x400+5+30")
        self.update()
        self.__c_speak_little.place_forget()
        self.__c_emotion_little.place_forget()
        self.__little_enabled = False
        self.__sequence_speak(self.__language.get_ph_normal_mode())

    def __mode_codehelp_normal(self):
        print("MODE CODEHELP NORMAL")

    def __mode_little(self):
        self.geometry("500x120+5+30")
        self.update()
        self.__c_speak_normal.place_forget()
        self.__c_emotion_normal.place_forget()
        self.__little_enabled = True
        self.__sequence_speak(self.__language.get_ph_little_mode())

    def __mode_codehelp_little(self):
        print("MODE CODEHELP LITTLE")

    # Methode qui gere l'update de l'interface

    def __update_during_assistant_reflect(self,firt_call:bool=False):
        if self.__th_reflect.is_alive():
            self.__change_img_load(self.__index_load)
            if firt_call:
                self.__assistant_load = True
                self.__c_speak_normal.place_forget()
                self.__c_emotion_little.place_forget()
                self.__c_emotion_normal.place_forget()
                self.__back_widget_normal.place_forget()
                if not self.__little_enabled:
                    self.__c_load_normal.place(x=0, y=0)
                else :
                    self.__c_load_little.place(x=0, y=0)
                self.update()
            self.__index_load += 1

            if self.__index_load >= len(self.__L_img_gui_load):
                self.__index_load = 0
            self.after(100,self.__update_during_assistant_reflect)
        else :
            self.__assistant_load = False
            nbSortie = self.__brain.getValeurSortie()
            listSortie = self.__brain.getListSortie()

            self.__treatment_out_assistant(nbSortie,listSortie)

    def __update__assistant(self):
        if not self.__setting_is_enabled :
            self.__timer += 1
            if self.__brain.updateAssistant():
                varOut = self.__brain.getValeurSortie()
                listOut = self.__brain.getListSortie()
                self.__treatment_out_assistant(varOut,listOut)
            elif self.__timer >= 10:
                if self.__timer == 10:
                    if not self.__little_enabled :
                        self.__c_speak_normal.place_forget()
                        self.__c_emotion_normal.place(x=0, y=0)
                    else :
                        self.__c_speak_little.place_forget()
                        self.__c_emotion_little.place(x=0, y=0)
                    self.update()

                self.__sequence_emotion()

        self.__manage_btn_open_fnc()

        self.after(1000,self.__update__assistant)

    # Methode qui agit sur la fenetre

    def __on_close(self):
        if askyesno("Atention", "Voulez-vous vraiment fermer Arrera Ryley ?"):
            self.title(self.__nameSoft)
            self.__gazelleUI.clearAllFrame()
            self.update()
            self.__sequence_stop()

            if self.__objOS.osWindows():
                os.kill(os.getpid(), signal.SIGINT)
            elif self.__objOS.osLinux() or self.__objOS.osMac():
                os.kill(os.getpid(), signal.SIGKILL)
        else :
            self.__sequence_speak(self.__language.get_ph_cancel_close())

    def __about(self):
        windows_about(nameSoft=self.__nameSoft,
                      iconFile="asset/icone/linux/icon.png",
                      version=self.__version,
                      copyright="Copyright Arrera Software by Baptiste P 2023-2026",
                      linkSource="https://github.com/Arrera-Software/Ryley",
                      linkWeb="https://arrera-software.fr/")

    def __windows_help_assistant(self,texte:str):
        winHelp = aTopLevel(width=500, height=600,title="Arrera Copilote : Aide Assistant",
                            icon=self.__emplacementIcon)
        labelTitleHelp = aLabel(winHelp, police_size=25,text="Copilote - Aide")
        aideView = aText(winHelp, width=475, height=500,wrap="word",police_size=20)

        self.__sequence_speak(self.__language.get_ph_help())

        aideView.insert_text(texte)
        labelTitleHelp.placeTopCenter()
        aideView.placeCenter()

    # Methode pour la gestion des parametre

    def __active_setting(self):
        if self.__little_enabled:
            self.geometry("500x400+5+30")
            self.update()
            self.__c_speak_little.place_forget()
            # self.__c_emotion_little.place_forget()
            self.__little_enabled = False
        self.__setting_is_enabled = True
        self.__c_load_normal.place_forget()
        self.__c_load_little.place_forget()
        self.__back_widget_normal.place_forget()
        self.__c_speak_normal.place_forget()
        self.__c_boot.place_forget()
        self.__gazelleUI.active()

    def __quit_setting(self):
        self.__gazelleUI.clearAllFrame()
        self.__sequence_speak(self.__language.get_ph_setting())
        self.__setting_is_enabled = False

    # Methode pour la gestion des btn qui ouvre les fnc
    def __manage_btn_open_fnc(self):
        if self.__brain.getTableur() :
            for btn in self.__L_btn_tableur_normal:
                btn.placeBottomRight()
        else :
            for btn in self.__L_btn_tableur_normal:
                btn.place_forget()

        if self.__brain.getWord():
            for btn in self.__L_btn_word_normal:
                btn.placeBottomLeft()
        else :
            for btn in self.__L_btn_word_normal:
                btn.place_forget()

        if self.__brain.getProject():
            for btn in self.__L_btn_project_normal:
                btn.placeBottomCenter()
        else :
            for btn in self.__L_btn_project_normal:
                btn.place_forget()
