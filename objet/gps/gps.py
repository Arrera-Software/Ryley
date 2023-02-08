import requests

class ville:
    def __init__(self,ville):
        url = "http://api.openweathermap.org/geo/1.0/direct?q="
        keyApi="19bfbee6112be5b3d9a64d4ccec72602"
        self.reponse = requests.get(url+ville+"&appid="+keyApi)
    def lat(self):
        if self.reponse.status_code == 400 :
            return "error"
        else :
            return str(self.reponse.json()[0]["lat"])
    
    def long(self):
        if self.reponse.status_code == 400 :
            return "error"
        else :
            return str(self.reponse.json()[0]["lon"])