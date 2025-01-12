from librairy.travailJSON import *

class CLanguageRyley :
    def __init__(self, fileLanguage:str, fileHelp:str,fileFirstBoot:str):
        self.__language = jsonWork(fileLanguage)
        self.__help = jsonWork(fileHelp)
        self.__firstBoot = jsonWork(fileFirstBoot)

    def getHelpTableur(self):
        return self.__help.lectureJSONList("tableur")

    def getHelpWord(self):
        return self.__help.lectureJSONList("word")

    def getHelpProjet(self):
        return self.__help.lectureJSONList("projet")