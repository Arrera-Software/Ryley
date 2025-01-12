from src.ryleyGUI import *
from arreraLynx.arreraLynx import *

class ryleyBoot:
    def __init__(self):
        # Ouverture JSON
        json = jsonWork("fichierJSON/configUser.json")
        # Declaration des var
        self.__sortieLynx = False

        # Verification de la configuration de l'assistant
        if ((json.lectureJSON("user") == "") and
                (json.lectureJSON("genre") == "")):
            self.__firstStart = True
        else:
            self.__firstStart = False
        del json

    def active(self):
        if (self.__firstStart):
            lynx = ArreraLynx("fichierJSON/configLynx.json",
                              "fichierJSON/configUser.json",
                              "fichierJSON/configNeuron.json")
            lynx.active()
            self.__sortieLynx = lynx.confiCreate()
        else :
            self.__sortieLynx = True

        self.__boot()


    def __boot(self):
        if (self.__sortieLynx == False):
            arrTk = CArreraTK()
            screen = arrTk.aTK(title="Arrera Ryley",resizable=False,width=500,height=350)
            imgCavas = arrTk.createArreraBackgroudImage(screen,
                                                        imageDark="asset/GUI/dark/NoConfig.png",
                                                        imageLight="asset/GUI/light/NoConfig.png",
                                                        width=500,height=350)
            labeltext = arrTk.createLabel(screen,
                                          text="Désoler mais vous avez pas configuer l'assistant correctement",
                                          ppolice="Arial",ptaille=20,
                                          pstyle="bold",bg="#041f75",
                                          fg="white",pwraplength=300,
                                          justify="left")
            btnConf = arrTk.createButton(screen,text="Configurer",ppolice="Arial",ptaille=20,
                                          pstyle="bold",command=lambda:self.__restartConf(screen))
            imgCavas.pack()
            labeltext.place(x=190,y=40)
            arrTk.placeBottomCenter(btnConf)
            arrTk.view()
        else :
            assistant = guiRyley("fichierJSON/configNeuron.json")
            assistant.active(self.__firstStart)

    def __restartConf(self,windows:ctk.CTk):
        windows.destroy()
        self.active()