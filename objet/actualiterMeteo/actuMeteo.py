import requests

class Actualiter :
    def __init__(self):
        self.api_key = "3b43e18afcf945888748071d177b8513"
        self.urlActuMondial = "https://newsapi.org/v2/everything?q=" + "actualités mondial" + "&apiKey=" + self.api_key + "&language=fr"
        self.urlActuFr = "https://newsapi.org/v2/everything?q=" + "actualités en français" + "&apiKey=" + self.api_key + "&language=fr"
        self.urlActuPolitique  =  "https://newsapi.org/v2/everything?q=" + "actualités politique" + "&apiKey=" + self.api_key + "&language=fr"
        self.urlActuCrypto =  "https://newsapi.org/v2/everything?q=" + "crypto money" + "&apiKey=" + self.api_key + "&language=fr"
        
    def Netoyage(self,dictionnnaire):
        titre = dictionnnaire["title"]
        return titre
    
    def recuperation(self):
        self.responseMondiale = requests.get(self.urlActuMondial)
        self.responseFr = requests.get(self.urlActuFr)
        self.reponsePoli = requests.get(self.urlActuPolitique)
        self.reponseCrypto = requests.get(self.urlActuCrypto)
        self.listactu = []
        if (self.responseMondiale.status_code == 200)and(self.responseFr.status_code == 200)and(self.reponsePoli.status_code == 200)and(self.reponseCrypto.status_code == 200):
            self.dataMondiale = self.responseMondiale.json()
            self.dataFr = self.responseFr.json()
            self.dataPoli = self.reponsePoli.json()
            self.dataCrypto = self.reponseCrypto.json()
            self.actu1 = self.Netoyage(self.dataMondiale["articles"][0])
            self.actu2 = self.Netoyage(self.dataMondiale["articles"][2])
            self.actu3 = self.Netoyage(self.dataFr["articles"][0])
            self.actu4 = self.Netoyage(self.dataFr["articles"][2])
            self.actu5 = self.Netoyage(self.dataPoli["articles"][0])
            self.actu6 = self.Netoyage(self.dataCrypto["articles"][0])
            self.listactu = [self.actu1 , self.actu2 ,self.actu3,self.actu4,self.actu5,self.actu6]
        else:
            self.listactu=["ereur","ereur","ereur","ereur","ereur","ereur"]
        return self.listactu
    

class meteo : 
    def __init__(self,latitude,longitude):
        keyApi="ecffd157b2cc9eacbd0d35a45c3dc047"
        url="https://api.openweathermap.org/data/2.5/weather?"
        self.reponse=requests.get(url+"lat="+str(latitude)+"&lon="+str(longitude)+"&lang=fr&units=metric&appid="+keyApi)
        #print(self.reponse)
        
    def temperature(self):
        if self.reponse.status_code == 400 :
            return "error"
        else : 
            return str(self.reponse.json()["main"]["temp"])
    
    def humiditer(self):
        if self.reponse.status_code == 400 :
            return "error"
        else : 
            
            return str(self.reponse.json()["main"]["humidity"])
    
    def description(self):
        if self.reponse.status_code == 400 :
            return "error"
        else : 
            return self.reponse.json()["weather"][0]["description"]