from librairy.travailJSON import*
from src.gestionRyley import *
from src.ryleyInterface import*

class Ryley :
    def __init__(self):
        self.configRyley = jsonWork("fichierJSON/ryleyConfig.json")
        self.configUser = jsonWork("fichierJSON/configUser.json")
        self.configNeuron = jsonWork("fichierJSON/configNeuron.json")
        #Objet
        self.gestionnaire =  gestionRL(self.configRyley) # Gestionnaire
        self.GUI = interfaceRyley(self.gestionnaire)


    def bootAssistant(self):
        self.GUI.fenetreRyley()
        self.GUI.activeRyley()
