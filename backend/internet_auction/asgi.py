# import os
#
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internet_auction.settings')
#
# application = get_asgi_application()


import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import auction.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internet_auction.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            auction.routing.websocket_urlpatterns
        )
    ),
})