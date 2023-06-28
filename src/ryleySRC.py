import speech_recognition as sr
import winsound
import time


class RyleySRC :
    def __init__(self,label,nom):
        self.label = label
        self.nom = nom
    
    def passageLigne(self,text, nbMots):
        mots = text.split()
        newText = ""
        ligne = ""
        for i, mot in enumerate(mots):
            ligne += mot + " "
            if (i + 1) % nbMots == 0:
                newText += ligne + "\n"
                ligne = ""
            elif i == len(mots) - 1:
                newText += ligne
        return newText
    
    def speak(self,text):
        self.label.config(justify="left")
        text = self.passageLigne(text,7)
        self.label.config(text=self.nom+": "+text)
        self.label.update()
    

class Micro :
    def __init__(self,entry):
        self.entry = entry
        pass
      
    def takeCommand(self):#Fonction micro et reconaissance vocal
        winsound.Beep(440, 500)
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:
                Requette=r.recognize_google(audio,language='fr')
                self.entry.insert(0,Requette)
                winsound.Beep(500, 440)
            except Exception as e:
                return "None" 
            time.sleep(1)
            return Requette  
    