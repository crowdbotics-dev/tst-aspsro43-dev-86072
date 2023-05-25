
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MailViewSet
router = DefaultRouter()
router.register('mail', MailViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
