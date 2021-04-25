# chat/consumers.py
import json
import requests
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        cambio_valuta = {'base': 'USD','symbols': 'GBP'}
        response = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=3c3087f3418c68c6b8cc8a12a6960840&symbols=EUR,AUD,USD,GBP,CAD,PLN")
        nostre_valute = response.json()

        #print(nostre_valute["rates"])
        self.send(text_data=json.dumps({
            #'message': message
            'message': str(nostre_valute["rates"])
        }))