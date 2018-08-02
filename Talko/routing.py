# create a routing configuration file for the chat app that has a route to the consumer
# The script is created on the app(talko) route  location


from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
from . import consumers
# (Point the routing confguration at the chat.routing module )
# Importing the AuthMiddleWareStack,URLRouter


application = ProtocolTypeRouter({
    # Http --> Django views is added by default
    websocket : AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer)

]