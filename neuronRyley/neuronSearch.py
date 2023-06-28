import re
from function.JSON import*
from function.internet import*
from src.ryleySRC import*

def Neuronsearch(var,fenetre,user,srcRyley:RyleySRC):
    moteurActuel = lectureJSON("setting/config.json","nameMoteur")
    if "recherche" in var or "Recherche" in var :
        if "recherche" in var :
            recherche = re.sub("recherche ","",var)
        else : 
            recherche = re.sub("Recherche ","",var)
        moteur = search(recherche)
        if moteurActuel == "duckduckgo" :
             moteur.duckduckgoSearch()
        else :
           if moteurActuel == "google" :
                moteur.googleSearch() 
           else : 
               if moteurActuel == "qwant" :
                    moteur.QwantSearch()
               else :
                   if moteurActuel == "ecosia":
                        moteur.EcosiaSearch()
                   else :
                       if moteurActuel == "brave":
                             moteur.braveSearch()
                       else :
                           if moteurActuel == "bing":
                                moteur.bingSearch()   
        srcRyley.speak("Voici le resultat de ta recherche")           
        return 1
    else :
        if "bigsearch" in var or "Bigsearch" in var :
                if "bigsearch" in var :
                    recherche = re.sub("bigsearch ","",var)
                else : 
                    recherche = re.sub("Bigsearch ","",var)
                search(recherche).GrandRecherche()
                srcRyley.speak("Voici les resultat de ta grand recherche")
        else :
            return 0