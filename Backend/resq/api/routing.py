from django.urls import re_path
from .consumers import HospitalConsumer

websocket_urlpatterns = [
    re_path(r'ws/hospitals/$', HospitalConsumer.as_asgi()),
]
