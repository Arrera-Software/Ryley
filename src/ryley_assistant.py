from brain.brain import ABrain,confNeuron
from lynx_gui.arrera_lynx import arrera_lynx
from src.ryley_gui import ryley_gui
from src.version_demon import demon,soft_config
from lib.arrera_tk import *

THEME_FILE = "asset/theme/theme_bleu.json"

SOFT_CONF = soft_config(
    name_soft="ryley",
    version="I2026-0.00"
)

class ryley_assistant():
    def __init__(self):
        self.__assistant_conf = confNeuron(
            name="Arrera Ryley",
            lang="fr",
            asset="asset/",
            icon="asset/icon/linux/icon.png",
            assistant_color="#041f75",
            assistant_texte_color="white",
            bute="",
            createur="Baptiste P",
            listFonction=[],
            moteurderecherche="google",
            etatService=1,
            etatTime=1,
            etatOpen=1,
            etatSearch=1,
            etatChatbot=1,
            etatApi=1,
            etatCodehelp=1,
            etatWork=1,
            etatSocket=1,
            lienDoc="www.google.com", # TODO : A changer plus tart
            fichierLangue="language/", # Path to language files
            fichierKeyword="keyword/",            # Path to keyword files
            voiceAssistant=False
        )

        # Demon de MAJ
        self.__demon = demon(SOFT_CONF, "https://arrera-software.fr/depots.json")

        # Demarage du reseau de neuron
        self.__assistant = ABrain(self.__assistant_conf)
        self.__gestionnaire = self.__assistant.getGestionnaire()

        # Var
        self.__firt_boot = self.__gestionnaire.getUserConf().getFirstRun()
        self.__state_conf = False

    def active(self):
        if self.__firt_boot:
            l = arrera_lynx(self.__gestionnaire,
                            "json_conf/configLynx.json",
                            THEME_FILE)
            self.__state_conf = l.return_state_lynx()
        else :
            self.__state_conf = True
        self.__boot()

    def __boot(self):
        if not self.__state_conf:
            pass # TODO : Faire la partie non conf
        else :
            assistant = ryley_gui("asset/icon/",
                                "icon",
                                self.__assistant,
                                THEME_FILE,
                                self.__demon.getVersionSoft())
            assistant.active(self.__firt_boot,self.__demon.checkUpdate())