from librairy.travailJSON import*
from src.gestionRyley import *
from src.ryleyInterface import*
from ObjetsNetwork.arreraNeuron import*
from arreraLynx.arreraLynx import*

class Ryley :
    def __init__(self):
        self.__configRyley = jsonWork("fichierJSON/ryleyConfig.json")
        self.__configUser = jsonWork("fichierJSON/configUser.json")
        self.__configNeuron = jsonWork("fichierJSON/configNeuron.json")
        self.__fichierLynx = jsonWork("fichierJSON/configLynx.json")
        #Objet
        self.gestionnaire =  gestionRL(self.__configRyley) # Gestionnaire
        self.networkNeuron = ArreraNetwork("fichierJSON/configUser.json","fichierJSON/configNeuron.json","fichierJSON/listFete.json")
        self.GUI = interfaceRyley(self.gestionnaire,self.networkNeuron)
    
    def __verifBoot(self):
        if not self.__configUser.lectureJSON("user") and not self.__configUser.lectureJSON("genre") :
            return False
        else :
            return True

    def __activeLynx(self,mode:int):
        screen = Tk()
        ArreraLynx(screen,self.__fichierLynx,self.__configUser,self.__configNeuron).active()
        screen.mainloop()
        if mode == 1 :
            self.GUI.windows()
            self.GUI.bootRyley()
            self.GUI.enableWindows()
        else :
            if mode == 2 :
                self.GUI.windows()
                self.GUI.bootCodehelp()
                self.GUI.enableWindows()

    def bootAssistant(self):
        if self.__verifBoot() == True : 
            self.GUI.windows()
            self.GUI.bootRyley()
            self.GUI.enableWindows()
        else :
            self.__activeLynx(1)

    def bootCodeHelp(self):
        if self.__verifBoot() == True : 
            self.GUI.windows()
            self.GUI.bootCodehelp()
            self.GUI.enableWindows()
        else :
            self.__activeLynx(2)