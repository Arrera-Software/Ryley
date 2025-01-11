from librairy.arrera_tk import CArreraTK
from ObjetsNetwork.arreraNeuron import *

VERSION = "I2025-1.00"

class guiRyley:
    def __init__(self, neuronConfigFile: str):
        # Boot ArreraTK
        self.__arrTK = CArreraTK()

        # Demarage Neuron Network
        self.__assistant = ArreraNetwork(neuronConfigFile)

        # Teste sur de l'OS hote
        objOS = OS()
        self.__windowsOS = objOS.osWindows()
        self.__linuxOS = objOS.osLinux()
        del objOS

        # Demarage de l'interface
        self.__screen = self.__arrTK.aTK(0,title="Ryley", resizable=False,
                                         width=500, height=600)

        # Definition des images
        emplacementLight = "asset/GUI/light/"
        emplacementDark = "asset/GUI/dark/"

        listIMG = ["top.png", "bottom.png","send.png"]
        # Creation des images

        imgSend = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[2],
                                           pathDark=emplacementDark + listIMG[2],
                                           tailleX=45, tailleY=30)

        # Frame
        self.__topBackgroup = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                      imageLight=emplacementLight + listIMG[0],
                                                                      imageDark=emplacementDark + listIMG[0],
                                                                      width=500, height=400)
        self.__bottomBackgroup = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                         imageLight=emplacementLight + listIMG[1],
                                                                         imageDark=emplacementDark + listIMG[1],
                                                                         width=500, height=70)
        self.__frameBackgroud = self.__arrTK.createFrame(self.__screen,
                                                         width=500, height=130,
                                                         bg="#081ec7",corner_radius=0)
        # Widget
        entryUser = self.__arrTK.createEntry(self.__frameBackgroud,
                                             ppolice="Arial", ptaille=25, width=300)

        btnSend = self.__arrTK.createButton(self.__frameBackgroud, text="Envoyer",
                                            ppolice="Arial", ptaille=20,
                                            pstyle="bold", image=imgSend)


        # Affichage des widgets
        #self.__arrTK.placeLeftCenter(entryUser)
        entryUser.place(relx=0.35, rely=0.3, anchor="center")
        self.__arrTK.placeRightCenter(btnSend)

    def active(self):
        self.__topBackgroup.pack()
        self.__bottomBackgroup.pack()
        self.__frameBackgroud.pack()
        self.__arrTK.view()


