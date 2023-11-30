from librairy.travailJSON import*

class gestionRL :
    def __init__(self,configRyley:jsonWork) :
        self.__configFile = configRyley
        self.__BGBottom = str
        self.__BGTop = str
        self.__BGTopCodehelpRight = str
        self.__BGTopCodehelpLeft = str
        self.__BGBottomCodehelp = str
        self.__BTNIconBack = str
        self.__BTNIconColorSelector = str
        self.__BTNIconGitHub = str
        self.__BTNIconLibrairy = str
        self.__BTNIconOrgaVar = str
        self.__BTNIconNoIcon = str
        self.__mainColor = str
        self.__secondColor = str
        self.__mainTextColor = str
        self.__secondTextColor = str
        self.__themeSet = False

    def setTheme(self):
        emplacementImage = "asset/interface/"
        emplacementImageCodehelp = "asset/codeHelp/"
        self.__BGBottom = emplacementImage+"BGBottom.png"
        self.__BGBottomCodehelp = emplacementImageCodehelp + "BGBottomCodeHelp.png"
        self.__secondColor = "#081ec7"
        self.__secondTextColor = "#ffffff"
        self.__BTNIconNoIcon = emplacementImageCodehelp+"BTN/BTNNoIcon.png"    
        if self.__configFile.lectureJSON("theme") == "light":
            emplacementImageCodehelpBTN = emplacementImageCodehelp+"BTN/Light/"
            self.__BGTop = emplacementImage + "BGTop-light.png"
            self.__BGTopCodehelpLeft = emplacementImageCodehelp+"BGTopCodeHelp-light-left.png"
            self.__BGTopCodehelpRight = emplacementImageCodehelp+"BGTopCodeHelp-light-right.png"
            self.__BTNIconBack = emplacementImageCodehelpBTN + "BTNback.png"
            self.__BTNIconColorSelector = emplacementImageCodehelpBTN + "BTNColorSelector.png"
            self.__BTNIconGitHub = emplacementImageCodehelpBTN + "BTNGithub.png"
            self.__BTNIconLibrairy = emplacementImageCodehelpBTN + "BTNLibrairy.png"
            self.__BTNIconOrgaVar = emplacementImageCodehelpBTN + "BTNOrgaVar.png"
            self.__mainColor = "#ffffff"
            self.__mainTextColor = "#000000"
        else :
            if self.__configFile.lectureJSON("theme") == "dark":
                emplacementImageCodehelpBTN = emplacementImageCodehelp+"BTN/Dark/"
                self.__BGTop = emplacementImage + "BGTop-dark.png"
                self.__BGTopCodehelpLeft = emplacementImageCodehelp+"BGTopCodeHelp-dark-left.png"
                self.__BGTopCodehelpRight = emplacementImageCodehelp+"BGTopCodeHelp-dark-right.png"
                self.__BTNIconBack = emplacementImageCodehelpBTN + "BTNback.png"
                self.__BTNIconColorSelector = emplacementImageCodehelpBTN + "BTNColorSelector.png"
                self.__BTNIconGitHub = emplacementImageCodehelpBTN + "BTNGithub.png"
                self.__BTNIconLibrairy = emplacementImageCodehelpBTN + "BTNLibrairy.png"
                self.__BTNIconOrgaVar = emplacementImageCodehelpBTN + "BTNOrgaVar.png"
                self.__mainColor = "#000000"
                self.__mainTextColor = "#ffffff"
            else :
                emplacementImageCodehelpBTN = emplacementImageCodehelp+"BTN/Light/"
                self.__BGTop = emplacementImage + "BGTop-light.png"
                self.__BGTopCodehelpLeft = emplacementImageCodehelp+"BGTopCodeHelp-light-left.png"
                self.__BGTopCodehelpRight = emplacementImageCodehelp+"BGTopCodeHelp-light-right.png"
                self.__BTNIconBack = emplacementImageCodehelpBTN + "BTNback.png"
                self.__BTNIconColorSelector = emplacementImageCodehelpBTN + "BTNColorSelector.png"
                self.__BTNIconGitHub = emplacementImageCodehelpBTN + "BTNGithub.png"
                self.__BTNIconLibrairy = emplacementImageCodehelpBTN + "BTNLibrairy.png"
                self.__BTNIconOrgaVar = emplacementImageCodehelpBTN + "BTNOrgaVar.png"
                self.__mainColor = "#ffffff"
                self.__mainTextColor = "#000000"    
        self.__themeSet = True
    
    def getBGTop(self):
        if self.__themeSet == True :
            return self.__BGTop
    
    def getBGBottom(self):
        if self.__themeSet == True :
            return self.__BGBottom
    
    def getMaincolor(self):
        if self.__themeSet == True :
            return self.__mainColor
    
    def getMainTextcolor(self):
        if self.__themeSet == True :
            return self.__mainTextColor
    
    def getSecondColor(self):
        if self.__themeSet == True :
            return self.__secondColor
    
    def getSecondTextColor(self):
        if self.__themeSet == True :
            return self.__secondTextColor
    
    def getBGTopCodeHelpLeft(self):
        if self.__themeSet == True :
            return self.__BGTopCodehelpLeft 
    
    def getBGBottomCodeHelp(self):
        if self.__themeSet == True :
            return self.__BGBottomCodehelp
    
    def getBGTopCodeHelpRight(self):
        if self.__themeSet == True : 
            return self.__BGTopCodehelpRight
    
    def getBTNIconBack(self):
        if self.__themeSet == True : 
            return self.__BTNIconBack
    
    def getBTNIconColorSelector(self):
        if self.__themeSet == True : 
            return self.__BTNIconColorSelector
        
    def getBTNIconGitHub(self):
        if self.__themeSet == True : 
            return self.__BTNIconGitHub
        
    def getBTNIconLibrairy(self):
        if self.__themeSet == True : 
            return self.__BTNIconLibrairy
        
    def getBTNIconOrgaVar(self):
        if self.__themeSet == True : 
            return self.__BTNIconOrgaVar
        
    def getBTNIconNoIcon(self):
        if self.__themeSet == True : 
            return self.__BTNIconNoIcon