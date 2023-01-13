from src.parole import*
from varriable import*
from objet.Horloge.AppHorloge import*

def Time(var,fenetre,user,label,nom):
    if "horloge" in var :
        speak("Ok je t'ouvre l'application horloge",label,nom)
        AppHorloge(mainColor,mainTextColor,"Ryley : Horloge","acceuil")
        return 1
    else :
        if "chronométre" in var or "chono" in var or "chonometre" in var :
            speak("Ok je t'ouvre le chronometre ",label,nom)
            AppHorloge(mainColor,mainTextColor,"Ryley : Horloge","chronometre")
            return 1
        else :
            if "minuteur" in var :
                speak("Ok je t'ouvre le minuteur",label,nom)
                AppHorloge(mainColor,mainTextColor,"Ryley : Horloge","minuteur")
                return 1
            else :
                return 0