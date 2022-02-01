from rest_framework import routers
from .api import MailingViewSet, ClientViewSet, MessageViewSet


router_mailing = routers.DefaultRouter()
router_mailing.register('api/mailing', MailingViewSet, 'mailing')

router_client = routers.DefaultRouter()
router_client.register('api/client', ClientViewSet, 'client')

router_message = routers.DefaultRouter()
router_message.register('api/message', MessageViewSet, 'message')

urlpatterns = router_message.urls + router_mailing.urls + router_client.urls


