#Utilizing advance paths
from django.urls import re_path
from app import consumers

#Using websockets url patterns instead of simple url patterns
websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\w+)/$',consumers.AdminConsumer.as_asgi()),
    
]