from lib.arrera_tk import *
from librairy.dectectionOS import OS
from gestionnaire.gestion import gestionnaire

class back_widget(aFrame):
    def __init__(self, master:aTk,gest_assistant:gestionnaire,key_gest:keyboad_manager,
                 dirImg:list, img_windows_mode:str,
                 img_mode:str,dectOS:OS,fonc_send:Callable,
                 fonc_mode:Callable,fonc_windows_mode:Callable,
                 fonc_setting:Callable):
        super().__init__(master,width=500,height=50)

        self.__l_dir = dirImg[0]
        self.__d_dir = dirImg[1]
        
        self.__master = master

        self.__gest_assistant = gest_assistant

        user = self.__entry_btn(img_mode)

        img_setting = aImage(width=30,height=30,path_light=self.__l_dir+"settings.png",path_dark=self.__d_dir+"settings.png")
        self.__btn_setting = aButton(self, text="", image=img_setting, width=30, height=30,command=fonc_setting)

        img_windows_mode = aImage(width=30, height=30, path_light=self.__l_dir + img_windows_mode, path_dark=self.__d_dir + img_windows_mode)
        self.__btn_windows_mode = aButton(self, text="", image=img_windows_mode, width=30, height=30)

        self.__btn_setting.placeLeftCenter()
        self.__btn_windows_mode.placeRightCenter()

        # Application comportement entry

        self.__entry.bind("<FocusIn>", self.__on_focus)
        self.__entry.bind("<FocusOut>", self.__reset_focus)

        if dectOS.osWindows():
            key_gest.add_key(27,lambda : master.focus())
            key_gest.add_key(13,fonc_send)
        elif dectOS.osLinux():
            key_gest.add_key(9,lambda : master.focus())
            key_gest.add_key(36,fonc_send)
        elif dectOS.osMac():
            key_gest.add_key(889192475,lambda : master.focus())
            key_gest.add_key(603979789,fonc_send)

        # Mise en place fonction dans les BTN

        self.__btn_send.configure(command=fonc_send)
        self.__btn_mode.configure(command=fonc_mode)
        self.__btn_windows_mode.configure(command=fonc_windows_mode)

        user.placeCenter()

    def __entry_btn(self,img_mode:str):
        f = aFrame(self,width=350,height=50)
        self.__entry = aEntry(f,width=200,police_size=20)

        img = aImage(width=30,height=30,path_light=self.__l_dir+"send.png",path_dark=self.__d_dir+"send.png")
        self.__btn_send = aButton(f, text="", image=img, width=30, height=30)

        img2 = aImage(width=30, height=30, path_light=self.__l_dir + img_mode, path_dark=self.__d_dir + img_mode)
        self.__btn_mode = aButton(f, text="", image=img2, width=30, height=30)

        self.__entry.placeBottomCenterNoStick()
        self.__btn_send.placeRightBottomNoStick()
        self.__btn_mode.placeLeftBottomNoStick()

        return f

    def __on_focus(self, event):
        # Agrandir l'entry
        self.__entry.configure(width=250)
        self.__entry.placeLeftBottomNoStick()

        # Afficher les boutons
        self.__btn_mode.place_forget()


    def __reset_focus(self, event=None):
        # Rétrécir l'entry
        self.__entry.configure(width=200)

        # Cacher les boutons
        self.__entry.placeBottomCenterNoStick()
        self.__btn_mode.placeLeftBottomNoStick()

        # Retirer le focus de l'entry
        self.__master.focus()

    def get_text_entry(self):
        return self.__gest_assistant.netoyageChaine(self.__entry.get().lower())

    def clear_entry(self):
        self.__entry.delete(0,END)

    def insert_text(self,text:str):
        self.__entry.insert(END,text)
