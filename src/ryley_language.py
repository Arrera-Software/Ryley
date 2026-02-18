from librairy.travailJSON import *

class ryley_language :
    def __init__(self, dir_language_file:str):
        self.__f_language= jsonWork(dir_language_file)

    def get_first_boot(self,nb:int): return self.__f_language.getContentJsonFlag(str(nb))

    def get_ph_setting(self): return self.__f_language.getContentJsonFlag("setting_close")

    def get_ph_help(self): return self.__f_language.getContentJsonFlag("aide")

    def get_ph_little_mode(self): return self.__f_language.getContentJsonFlag("little_mode")

    def get_ph_normal_mode(self): return self.__f_language.getContentJsonFlag("normal_mode")

    def get_ph_cancel_close(self): return self.__f_language.getContentJsonFlag("cancel_stop")

    def get_ph_codehelp(self,nb:int): return self.__f_language.getContentJsonFlag("codehelp"+str(nb))