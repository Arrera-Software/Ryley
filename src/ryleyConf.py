from librairy.travailJSON import *
from pathlib import Path
from librairy.dectectionOS import *

BASECONF = {"theme": "light"}

class RyleyConf:
    def __init__(self):
        self.__osDect = OS()
        self.__firstRun = False
        # Mise en place du chemin du fichier de configuration utilisateur
        if self.__osDect.osLinux() or self.__osDect.osMac():
            home = Path.home()
            self.__ryleySettingPath = str(home) + "/.config/assistant/ryley/ryley-config.json"
        elif self.__osDect.osWindows():
            home = Path.home() / "AppData" / "Roaming"
            self.__ryleySettingPath = str(home) + "/assistant/ryley/ryley-config.json"
        else :
            self.__ryleySettingPath = None


        if not Path(self.__ryleySettingPath).is_file():
            path = Path(self.__ryleySettingPath)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8") as f:
                json.dump(BASECONF, f, ensure_ascii=False, indent=2)

    def getRyleySettingPath(self):
        return self.__ryleySettingPath