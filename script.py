from setting.setting import *

var = int(input("1.Parametre\n0.quitter\n"))
match var :
    case 1 :
        Setting()
    case 0 :
        print("Ok")