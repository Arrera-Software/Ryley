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

        listIMG = ["top.png",
                   "bottom.png",
                   "send.png",
                   "settings.png",
                   "iconRyleyCodehelp.png"]
        # Creation des images

        imgSend = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[2],
                                           pathDark=emplacementDark + listIMG[2],
                                           tailleX=30, tailleY=30)
        imgPara = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[3],
                                             pathDark=emplacementDark + listIMG[3],
                                             tailleX=30, tailleY=30)

        imgCodehelp = self.__arrTK.createImage(pathLight=emplacementLight + listIMG[4],
                                             pathDark=emplacementDark + listIMG[4],
                                             tailleX=30, tailleY=30)

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
        # Entry
        self.__entryUser = self.__arrTK.createEntry(self.__frameBackgroud,
                                             ppolice="Arial", ptaille=25, width=350)

        # Bouton
        btnSend = self.__arrTK.createButton(self.__frameBackgroud,image=imgSend,
                                            width=40, height=40,
                                            bg="#3b4bca",hoverbg="#051484")

        btnPara = self.__arrTK.createButton(self.__frameBackgroud,image=imgPara,
                                            width=40, height=40,
                                            bg="#3b4bca",hoverbg="#051484")

        btnCodehelp = self.__arrTK.createButton(self.__frameBackgroud,image=imgCodehelp,
                                                width=40,height=40,
                                                bg="#3b4bca", hoverbg="#051484")

        # Label
        self.__lparole = self.__arrTK.createLabel(self.__topBackgroup,
                                                  bg="#041f75", fg="white",
                                                  ppolice="Arial",pstyle="bold",
                                                  ptaille=18,justify="left")

        # Affichage des widgets
        self.__entryUser.place(relx=0.40, rely=0.3, anchor="center")
        btnSend.place(relx=0.90, rely=0.3, anchor="center")
        self.__lparole.place(x=55, y=280)

        self.__arrTK.placeBottomLeft(btnPara)
        self.__arrTK.placeBottomRight(btnCodehelp)

    def active(self):
        self.__topBackgroup.pack()
        self.__bottomBackgroup.pack()
        self.__frameBackgroud.pack()
        self.__arrTK.view()


    def __paroleRyley(self, text: str):
        if text != "":
            self.__lparole.config(text=text)
            self.__entryUser.delete(0, END)