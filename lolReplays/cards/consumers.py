import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('connected')
        self.accept()
    
    def disconnect(self, close_code):
        pass

    def reveive(self, text_data):
        print("Received text")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

