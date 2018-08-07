# create a routing configuration file for the chat app that has a route to the consumer
# The script is created on the app(talko) route  location
from django.conf.urls import url
from . import consumers

# (Point the routing confguration at the Talko.routing module )
# Importing the AuthMiddleWareStack,URLRouter


websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),

]

