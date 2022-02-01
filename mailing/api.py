from .models import Mailing, Client, Message
from rest_framework import viewsets, permissions
from .serializer import MailingSerializer, MessageSerializer, ClientSerializer

class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MailingSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MessageSerializer