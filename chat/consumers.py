import json
#import jwt
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class DeviceConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, data):
        #data = json.loads(text_data)
        message_type = data["type"]
        if message_type == 'auth':
            await self.authenticate_device(data)
        elif message_type == 'status':
            await self.handle_status_message(data)
        elif message_type == 'keep_alive':
            await self.handle_keep_alive(data)
            
        # # Send message to room group
        # await self.channel_layer.group_send(
        #     self.room_group_name, {"type": "chat.message", "message": message}
        # )

    async def authenticate_device(self, data):
        # token = data["token"]
        # try:
        #     decoded_payload = jwt.decode(token probs)
        #     device_id = decoded_payload['device_id']
            
        #     # Perform additional authentication checks if needed
            
        #     # If authenticated, acknowledge and welcome the device
        #     await self.send(json.dumps({
        #         'type': 'auth_success',
        #         'message': 'Device authenticated successfully.'
        #     }))
        # except (jwt.InvalidTokenError, OR DEVICE DOES NOT EXIST):
        #     await self.send(json.dumps({
        #         'type': 'auth_error',
        #         'message': 'Authentication failed. Invalid token or device.'
        #     }))
        pass
        
    async def handle_status_message(self, data):
        status_message = data["status"]
        # Process and store the status message as needed
        pass

    async def handle_keep_alive(self, data):
        keep_alive_message = data["message"]
        # Handle keep-alive messages from devices
        pass

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))