import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name # a pointer to the channel layer's channel name
        )

        await self.channel_layer.group_send( # send a message to the group as soon as we connect
            self.room_group_name,
            {
                'type' : 'tester message',
                'tester' : 'hello_universe',
            }
        )
    
    async def tester_message(self, event):
        tester = event['tester']

        await self.send(text_data=json.dumps({
            'tester' : tester,
        }))

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name    
        )