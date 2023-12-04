class codeHelpNeuron :
    def __init__(self,searchDoc,github,selecteurColor,librairy,orga):
        self.searchDoc =  searchDoc
        self.__github = github
        self.__selecteurColor = selecteurColor
        self.__lib = librairy
        self.__orgaVar = orga

    def neuron(self,requette:str):
        texte =  ""
        var = 0
        if (("doc microsoft" in requette )or ("learn" in requette) or ("visual" in requette)) :
            requette = requette.replace("doc microsoft","")
            requette = requette.replace("learn","")
            requette = requette.replace("visual","")
            if self.searchDoc.rechercheMicrosoft(requette) == True :
                texte = "Ouverture de la documentation de microsoft"
            else :
                texte = "Une erreur c'est produite lors\nde l'Ouverture de la documentation de microsoft"
            var = 1
        else :
            if ("doc" in requette) : 
                requette = requette.replace("doc","")
                print(requette)
                if self.searchDoc.rechercheDevDoc(requette) == True :
                    texte = "Recherche sur DevDoc"
                else :
                    texte = "Une erreur c'est produite"
                var = 1
            else :
                if "liste depos" in requette or "depos github" in requette or "github depos" in requette :
                    texte = "Voici la liste de vos depot"
                    self.__github.GUI()
                    self.__github.GUIListDepos()
                    var = 1
                else :
                    if "github search" in requette : 
                        texte = "Recherche sur github"
                        requette.replace("github search","")
                        self.__github.search(requette)
                        var = 1
                    else :
                        if "couleur" in requette :
                            texte ="Ouverture du colors selector"
                            self.__selecteurColor.bootSelecteur()
                            var = 1
                        else :
                            if "organisateur de varriable" in requette or "orga var" in requette :
                                texte ="Ouverture de l'organisateur de varriable"
                                self.__orgaVar.bootOrganisateur()
                                var = 1
                            else :
                                if "librairy" in requette or "lib" in requette :
                                    texte = "Ouverture de la librairy Arrera"
                                    self.__lib.librairy()
                                    var = 1
                                else :
                                    if "github" in requette :
                                        texte = "Ouverture de l'interface github"
                                        self.__github.GUI()
                                        var = 1
        return var,texte