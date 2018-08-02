from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import Talko.routing
application = ProtocolTypeRouter({
     # Http --> Django views is added by default
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            Talko.routing.websocket_urlpatterns
        )
    ),
    
})
