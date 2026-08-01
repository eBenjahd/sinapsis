import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, Message


# LO TRANSFORMAMOS PARA QUE SE PUEDA LLAMAR LUEGO COMO AWAIT
@database_sync_to_async
def create_message(room,user,content):
    return Message.objects.create(
        room = room,
        user = user,
        content = content
    )

@database_sync_to_async
def get_room(room_id):
    return Room.objects.get(id=room_id)


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        """
        Se ejecuta una única vez cuando el cliente intenta abrir
        un WebSocket.
        """

        print("Cliente conectado")
        print(self.scope.keys())

        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]

        self.room = await get_room(self.room_id)

        self.group_name = f"chat_{self.room_id}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        print(self.room)

        await self.accept()

    async def receive(self, text_data):
        """
        Se ejecuta cada vez que el cliente envía un mensaje.
        """

        data = json.loads(text_data)

        content = data.get('content')
        print(data)

        await create_message(
            room = self.room,
            user = self.scope['user'],
            content = content   
        )

    async def disconnect(self, close_code):
        """
        Se ejecuta cuando el cliente cierra el WebSocket.
        """

        print(f"Cliente desconectado. Código: {close_code}")