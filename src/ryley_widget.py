from lib.arrera_tk import *

class back_widget(aFrame):
    def __init__(self, master, dirImg:list, img_windows_mode:str,img_mode:str):
        super().__init__(master,width=500,height=50)

        self.__l_dir = dirImg[0]
        self.__d_dir = dirImg[1]


        user = self.__entry_btn(img_mode)

        img_setting = aImage(width=30,height=30,path_light=self.__l_dir+"settings.png",path_dark=self.__d_dir+"settings.png")
        self.__btn_setting = aButton(self, text="", image=img_setting, width=30, height=30)

        img_windows_mode = aImage(width=30, height=30, path_light=self.__l_dir + img_windows_mode, path_dark=self.__d_dir + img_windows_mode)
        self.__btn_windows_mode = aButton(self, text="", image=img_windows_mode, width=30, height=30)

        self.__entry.bind("<FocusIn>", self.on_focus)
        self.__entry.bind("<FocusOut>", self.reset_focus())

        self.__btn_setting.placeLeftCenter()
        self.__btn_windows_mode.placeRightCenter()
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

    def on_focus(self, event):
        # Agrandir l'entry
        self.__entry.configure(width=250)
        self.__entry.placeLeftBottomNoStick()

        # Afficher les boutons
        self.__btn_mode.place_forget()


    def reset_focus(self, event=None):
        # Rétrécir l'entry
        self.__entry.configure(width=200)

        # Cacher les boutons
        self.__entry.placeBottomCenterNoStick()
        self.__btn_mode.placeLeftBottomNoStick()

        # Retirer le focus de l'entry
        self.focus()