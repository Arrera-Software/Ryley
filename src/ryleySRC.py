import speech_recognition as sr
import winsound
import time


class RyleySRC :
    def passageLigne(text, nbMots):
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
    
    def speak(text,label,nom):
        label.config(justify="left")
        text = RyleySRC.passageLigne(text,7)
        label.config(text=nom+": "+text)
        label.update()
    
    def takeCommand(entry):#Fonction micro et reconaissance vocal
        winsound.Beep(440, 500)
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:
                Requette=r.recognize_google(audio,language='fr')
                entry.insert(0,Requette)
                winsound.Beep(500, 440)
            except Exception as e:
                return "None" 
            time.sleep(1)
            return Requette
    