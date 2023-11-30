from librairy.travailJSON import*
from src.gestionRyley import *
from src.ryleyInterface import*
from ObjetsNetwork.arreraNeuron import*

class Ryley :
    def __init__(self):
        self.configRyley = jsonWork("fichierJSON/ryleyConfig.json")
        self.configUser = jsonWork("fichierJSON/configUser.json")
        self.configNeuron = jsonWork("fichierJSON/configNeuron.json")
        #Objet
        self.gestionnaire =  gestionRL(self.configRyley) # Gestionnaire
        self.networkNeuron = ArreraNetwork("fichierJSON/configUser.json","fichierJSON/configNeuron.json","fichierJSON/listFete.json")
        self.GUI = interfaceRyley(self.gestionnaire,self.networkNeuron)

    def bootAssistant(self):
        self.GUI.windows()
        self.GUI.bootRyley()
        self.GUI.enableWindows()

    def bootCodeHelp(self):
        self.GUI.windows()
        self.GUI.bootCodehelp()
        self.GUI.enableWindows()