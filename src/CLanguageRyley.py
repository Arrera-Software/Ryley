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

    def getPhOpenActu(self):
        return self.__language.lectureJSON("phOpenActu")

    def getPhErreurActu(self):
        return self.__language.lectureJSON("phErreurActu")

    def getPhErreurResumerActu(self):
        return self.__language.lectureJSON("phErreurResumer")

    def getPhResumerActu(self):
        return self.__language.lectureJSON("phResumerActu")

    def getPhResumerAgenda(self):
        return self.__language.lectureJSON("phResumerAgenda")

    def getPhResumerAll(self):
        return self.__language.lectureJSON("phResumerAll")

    def getPhErreurResumerAll(self):
        return self.__language.lectureJSON("phErreurResumerAll")