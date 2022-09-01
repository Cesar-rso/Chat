from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Messages, Chatroom
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
import json


class ChatRoomConsumer(AsyncWebsocketConsumer):

    # def __init__(self):
    #     self.room_name = ''
    #     self.room_group_name = ''

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

        await save_message(self.room_name, username, message)


@database_sync_to_async
def save_message(room, username, msg):
    chatroom = Chatroom.objects.get(room_name=room)
    user_querie = User.objects.get(username=username)
    sent_message = Messages(room=chatroom, user=user_querie, message=msg)
    sent_message.save()
