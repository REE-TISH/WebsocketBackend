import os
import django
from channels.routing import get_default_application,ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import PleaseWork.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()
application = ProtocolTypeRouter({
    "http":get_default_application(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            PleaseWork.routing.websocket_urlpatterns
        )
    )
})
