from librairy.travailJSON import*
from src.gestionRyley import *
from src.ryleyInterface import*
from ObjetsNetwork.arreraNeuron import*
from arreraLynx.arreraLynx import*

class Ryley :
    def __init__(self):
        #Objet
        gestionnaire =  gestionRL(jsonWork("fichierJSON/ryleyConfig.json")) # Gestionnaire
        networkNeuron = ArreraNetwork("fichierJSON/configNeuronTutoiment.json")
        self.GUI = interfaceRyley(gestionnaire,networkNeuron)
    
    def __verifBoot(self):
        configUser = jsonWork("fichierJSON/configUser.json")
        if not configUser.lectureJSON("user") and not configUser.lectureJSON("genre") :
            return False
        else :
            return True

    def __activeLynx(self):
        screen = Tk()
        lynx = ArreraLynx(screen,
                          jsonWork("fichierJSON/configLynx.json"),
                          jsonWork("fichierJSON/configUser.json"),
                          jsonWork("fichierJSON/configNeuron.json") )
        lynx.active()
        screen.mainloop()
        if lynx.confiCreate() == True :
            self.GUI.windows()
            self.GUI.bootRyley()
            self.GUI.enableWindows()
        else :
            showwarning("La configuration mauvaise","Vous avez pas entre votre nom et genre dans l'outil de configuration")

    def bootAssistant(self):
        if self.__verifBoot() == True : 
            self.GUI.windows()
            self.GUI.bootRyley()
            self.GUI.enableWindows()
        else :
            self.__activeLynx()
    
    def bootPara(self):
        self.GUI.windows()
        self.GUI.bootPara()
        self.GUI.enableWindows()