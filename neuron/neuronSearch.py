import requests
import webbrowser
import re
from src.parole import*
from function.JSON import*
from function.internet import*

def search(var,fenetre,user,label,nom):
    moteurActuel = lectureJSON("setting/config.json","nameMoteur")
    
    if "recherche" in var or "Recherche" in var :
        if "recherche" in var :
            recherche = re.sub("recherche ","",var)
        else : 
            recherche = re.sub("Recherche ","",var)
        if moteurActuel == "duckduckgo" :
            duckduckgoSearch(recherche)
        else :
           if moteurActuel == "google" :
               googleSearch(recherche) 
           else : 
               if moteurActuel == "qwant" :
                   QwantSearch(recherche)
               else :
                   if moteurActuel == "ecosia":
                        EcosiaSearch(recherche)
                   else :
                       braveSearch(recherche)             
        return 1
    else :
        if "bigsearch" in var or "Bigsearch" in var :
                if "bigsearch" in var :
                    recherche = re.sub("bigsearch ","",var)
                else : 
                    recherche = re.sub("Bigsearch ","",var)
                GrandRecherche(recherche)
        else :
            return 0