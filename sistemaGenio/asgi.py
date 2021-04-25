import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import valute.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistemaGenio.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            valute.routing.websocket_urlpatterns
        )
    ),
})