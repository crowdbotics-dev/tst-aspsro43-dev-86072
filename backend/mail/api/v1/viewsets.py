from rest_framework import authentication
from mail.models import Mail
from .serializers import MailSerializer
from rest_framework import viewsets

class MailViewSet(viewsets.ModelViewSet):
    serializer_class = MailSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Mail.objects.all()