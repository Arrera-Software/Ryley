from API.API import*
from src.ryleySRC import *
from function.traduction import*
from function.internet import*
import webbrowser
from objet.Calcule.calcule import*

def Main(var,fenetre,user,label,nom):
    gDrive = lectureJSON("setting/config.json","lienDrive")
    lienEDT = lectureJSON("setting/config.json","lienEDT")
    lienAgenda = lectureJSON("setting/config.json","lienAngenda")
    lienSite1 = lectureJSON("setting/config.json","lienSite1")
    nameSite1 = lectureJSON("setting/config.json","NameSite1")
    lienSite2 = lectureJSON("setting/config.json","lienSite2")
    nameSite2 = lectureJSON("setting/config.json","NameSite2")
    lienSite3 = lectureJSON("setting/config.json","lienSite3")
    nameSite3 = lectureJSON("setting/config.json","NameSite3")
    if "Calcule" in var or "calcule" in var and "Calcul" in var or "calcul" in var :
        Calcule(mainColor,mainTextColor,"Ryley : Calculatrice")
        return 1
    else :
        if "meteo" in var:
            Meteo(label,nom)
            return 1
        else :
            if "traduction" in var or "Traduction" in var or "trad" in var:
                Traduction()
                return 1
            else :
                if "Drive" in var or "Google Drive" in var or "drive" in var:
                    RyleySRC.speak("Voici Google Drive ;)",label,nom)
                    time.sleep(1.75)
                    webbrowser.open(gDrive)
                    return 1
                else :
                    if "agenda" in var or "taff" in var or "devoirs" in var or "devoir" in var:
                        RyleySRC.speak("Voila ce que tu as à faire : ",label,nom)
                        time.sleep(1.75)
                        webbrowser.open(lienAgenda)
                        return 1
                    else :
                        if "emploi du temps" in var or "edt" in var or "planning" in var or "emploi du tps" in var :
                            RyleySRC.speak("Tiens, ton planning des jours à venir :",label,nom)
                            time.sleep(1.75)
                            webbrowser.open(lienEDT)
                            return 1
                        else :
                            if nameSite1 in var:
                                RyleySRC.speak("Voila ! ",label,nom)
                                time.sleep(1.25)
                                webbrowser.open(lienSite1)
                                return 1
                            else :
                                if nameSite2 in var:
                                    RyleySRC.speak("Et voici ! ",label,nom)
                                    time.sleep(1.25)
                                    webbrowser.open(lienSite2)
                                    return 1
                                else :
                                    if nameSite3 in var:
                                        RyleySRC.speak("Tiens ! ",label,nom)
                                        time.sleep(1.25)
                                        webbrowser.open(lienSite3)
                                        return 1
                                    else :
                                        if "actu" in var or "actualité" in var or "news" in var :
                                            Resumeactu(label,nom)
                                            return 1
                                        else :
                                            return 0