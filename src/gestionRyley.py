from librairy.travailJSON import*

class gestionRL :
    def __init__(self,configRyley:jsonWork) :
        self.configFile = configRyley
        self.BGBottom = str
        self.BGTop = str
        self.BGTopCodehelpRight = str
        self.BGTopCodehelpLeft = str
        self.BGBottomCodehelp = str
        self.mainColor = str
        self.secondColor = str
        self.mainTextColor = str
        self.secondTextColor = str
        self.themeSet = False

    def setTheme(self):
        emplacementImage = "asset/interface/"
        emplacementImageCodehelp = "asset/codeHelp/"
        self.BGBottom = emplacementImage+"BGBottom.png"
        self.BGBottomCodehelp = emplacementImageCodehelp + "BGBottomCodeHelp.png"
        self.secondColor = "#081ec7"
        self.secondTextColor = "#ffffff"
        if self.configFile.lectureJSON("theme") == "light":
            self.BGTop = emplacementImage + "BGTop-light.png"
            self.BGTopCodehelpLeft = emplacementImageCodehelp+"BGTopCodeHelp-light-left.png"
            self.BGTopCodehelpRight = emplacementImageCodehelp+"BGTopCodeHelp-light-right.png"
            self.mainColor = "#ffffff"
            self.mainTextColor = "#000000"
        else :
            if self.configFile.lectureJSON("theme") == "dark":
                self.BGTop = emplacementImage + "BGTop-dark.png"
                self.BGTopCodehelpLeft = emplacementImageCodehelp+"BGTopCodeHelp-dark-left.png"
                self.BGTopCodehelpRight = emplacementImageCodehelp+"BGTopCodeHelp-dark-right.png"
                self.mainColor = "#000000"
                self.mainTextColor = "#ffffff"
            else :
                self.BGTop = emplacementImage + "BGTop-light.png"
                self.BGTopCodehelpLeft = emplacementImageCodehelp+""
                self.BGTopCodehelpRight = emplacementImageCodehelp+""
                self.mainColor = "#ffffff"
                self.mainTextColor = "#000000"
        
        self.themeSet = True
    
    def getBGTop(self):
        if self.themeSet == True :
            return self.BGTop
    
    def getBGBottom(self):
        if self.themeSet == True :
            return self.BGBottom
    
    def getMaincolor(self):
        if self.themeSet == True :
            return self.mainColor
    
    def getMainTextcolor(self):
        if self.themeSet == True :
            return self.mainTextColor
    
    def getSecondColor(self):
        if self.themeSet == True :
            return self.secondColor
    
    def getSecondTextColor(self):
        if self.themeSet == True :
            return self.secondTextColor
    
    def getBGTopCodeHelpLeft(self):
        if self.themeSet == True :
            return self.BGTopCodehelpLeft 
    
    def getBGBottomCodeHelp(self):
        if self.themeSet == True :
            return self.BGBottomCodehelp
    
    def getBGTopCodeHelpRight(self):
        if self.themeSet == True : 
            return self.BGTopCodehelpRight
