from objet.codeHelp.codeHelp import*

def neuronCodeHelp(var,fenetre,user,label,nom,entry,cadre,button,optionMenu,varChoix,fnc,cadre2,labelIndication,menu):
    if "doc code" in var or "documentation" in var or "devdoc" in var or "DevDoc" in var:
        CodeHelp.rechercheDoc(cadre,entry,label,button,optionMenu,varChoix,nom,fnc)
        return 2
    else :
        if "codeHelp" in var or "codehelp" in var or "Codehelp" in var:
            CodeHelp(cadre2,entry,label,button,optionMenu,varChoix,nom,fnc,labelIndication,"1",menu,fenetre)
            return 1
        else :
            if "github" in var :
                CodeHelp.PageGithub(cadre2,entry,label,button,nom,fnc,labelIndication)
                return 2
            else:
                if "tokenSave" in var :
                    CodeHelp.githubSaveToken(cadre2,entry,label,button,nom,fnc,labelIndication)
                    return 2 
                else :
                    if "userSave" in var :
                        CodeHelp.githubSaveUser(cadre2,entry,label,button,nom,fnc,labelIndication)
                        return 2 
                    else :
                        if "application code" in var or "app code" in var :
                            CodeHelp(cadre2,entry,label,button,optionMenu,varChoix,nom,fnc,labelIndication,"2",menu,fenetre)
                            return 2
                        else :
                            return 0