from setting.setting import *
from routine.ryleyRoutine import*

rep = int(input("1.Parametre\n2.Routine\n0.Quitter\n"))
match rep:
    case 1 :
        Setting()
    case 2 :
        ryleyRoutine()
    case other :
        print("Sa corespont pas")