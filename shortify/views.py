from django.shortcuts import get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets

from .models import ShortLink
from .serializers import ShortLinkSerializer


class ShortLinkViewSet(viewsets.ModelViewSet):
    serializer_class = ShortLinkSerializer

    def get_queryset(self):
        return ShortLink.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RedirectView(View):
    def get(self, request, code: str, *args, **kwargs):
        link = get_object_or_404(ShortLink, code=code)
        return redirect(link.url)
