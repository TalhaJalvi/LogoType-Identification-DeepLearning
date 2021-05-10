# Routing inside our chat
from channels.auth import AuthMiddlewareStack
#Some mechanism so we can utilize routing
from channels.routing import ProtocolTypeRouter, URLRouter
import app.routing


#Like urls in wsgi we use for assyncronious below
#When we get websocket request this is how to route it

application = ProtocolTypeRouter({
    #To utilize django authentication system we wrap it in django auth
    'websocket':AuthMiddlewareStack(
        #Now defining our routing
        URLRouter(
           app.routing.websocket_urlpatterns
        )
    ),

})