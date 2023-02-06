from setting.setting import *
from routine.ryleyRoutine import*
from objet.codeHelp.codeHelp import*

rep = int(input("1.Parametre\n2.Routine\n3.Organisateur de varriable\n0.Quitter\n"))
match rep:
    case 1 :
        Setting()
    case 2 :
        ryleyRoutine()
    case 3 :
        CodeHelp.orgranisateurVarriable()
    case other :
        print("Sa corespont pas")