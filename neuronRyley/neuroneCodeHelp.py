from objet.codeHelp.codeHelp import*

def neuronCodeHelp(var,fenetre,user,label,nom,entry,cadre,button,optionMenu,varChoix,fnc,cadre2):
    if "doc code" in var or "documentation" in var or "devdoc" in var or "DevDoc" in var:
        CodeHelp(cadre2,entry,label,button,optionMenu,varChoix,nom,fnc)
        CodeHelp.rechercheDoc(cadre,entry,label,button,optionMenu,varChoix,nom,fnc)
        return 2
    else :
        return 0