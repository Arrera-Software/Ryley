from src.ryleySRC import *
from src.varriable import*
from objet.Horloge.AppHorloge import*

def Time(var,fenetre,user,label,nom):
    if "application horloge" in var :
        RyleySRC.speak("Ok je t'ouvre l'application horloge",label,nom)
        AppHorloge(mainColor,mainTextColor,"Ryley : Horloge","acceuil")
        return 1
    else :
        if "chronomètre" in var or "chrono" in var or "chonometre" in var :
            RyleySRC.speak("Ok je t'ouvre le chronometre ",label,nom)
            AppHorloge(mainColor,mainTextColor,"Ryley : Horloge","chronometre")
            return 1
        else :
            if "minuteur" in var :
                RyleySRC.speak("Ok je t'ouvre le minuteur",label,nom)
                AppHorloge(mainColor,mainTextColor,"Ryley : Horloge","minuteur")
                return 1
            else :
                if "horloge" in var :
                    RyleySRC.speak("Ok je t'ouvre l'application horloge",label,nom)
                    AppHorloge(mainColor,mainTextColor,"Ryley : Horloge","horloge")
                    return 1
                else :
                    return 0