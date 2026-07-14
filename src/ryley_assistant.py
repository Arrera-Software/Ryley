from brain.brain import confNeuron
from src.ryley_gui import ryley_gui
from config.tiger_demon import tiger_demon

THEME_FILE = "asset/theme/theme_bleu.json"

VERSION = "dev"

class ryley_assistant():
    def __init__(self):
        self.__assistant_conf = confNeuron(
            name="Arrera Ryley",
            lang="fr",
            asset="asset/",
            icon="asset/icone/linux/icon.png",
            assistant_color="#041f75",
            assistant_texte_color="white",
            bute="Je suis un assistant spécialisé dans le développement informatique, la bureautique et l'organisation quotidienne.",
            createur="Baptiste P",
            listFonction=["Ouvrir une application",
                          "Aider aux recherches sur Internet",
                          "Donner la météo",
                          "Faire un résumé des actualités",
                          "Aider à organiser son travail",
                          "Donner l'heure",
                          "Créer des projets",
                          "Éditer des fichiers Word",
                          "Éditer des tableurs",
                          "Outil d'aide au développement informatique"],
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
            lienDoc="https://arrera-software.fr/docRyley",
            fichierLangue="language/", # Path to language files
            fichierKeyword="keyword/",            # Path to keyword files
            voiceAssistant=False
        )

        # Demon de MAJ
        self.__demon = tiger_demon("ryley",VERSION)

    def active(self):
        self.__boot()

    def __boot(self):
        assistant = ryley_gui(iconFolder="asset/icone/",iconName="icon",
                              conf=self.__assistant_conf,theme_file=THEME_FILE,
                              version=self.__demon.get_local_version())
        assistant.active(self.__demon.checkUpdate())