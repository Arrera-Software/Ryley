from librairy.travailJSON import *

class ryley_language :
    def __init__(self, dir_language_file:str):
        self.__f_language= jsonWork(dir_language_file)

    def get_first_boot(self,nb:int): return self.__f_language.getContentJsonFlag(str(nb))

    def get_ph_setting(self): return self.__f_language.getContentJsonFlag("setting_close")

    def get_ph_help(self): return self.__f_language.getContentJsonFlag("aide")