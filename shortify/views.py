from rest_framework import viewsets

from .models import ShortLink
from .serializers import ShortLinkSerializer


class ShortLinkViewSet(viewsets.ModelViewSet):
    serializer_class = ShortLinkSerializer

    def get_queryset(self):
        return ShortLink.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
