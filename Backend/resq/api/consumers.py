import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Hospital
from django.core.serializers.json import DjangoJSONEncoder

class HospitalConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        hospitals = list(Hospital.objects.values())  # Get latest data
        await self.send(text_data=json.dumps({"hospitals": hospitals}, cls=DjangoJSONEncoder))
