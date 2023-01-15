import speech_recognition as sr
import winsound
import time


class RyleySRC :
    def speak(text,label,nom):
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