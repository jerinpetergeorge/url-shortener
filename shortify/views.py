from django.shortcuts import get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets

from .cache import ShortLinkCache
from .models import ShortLink
from .serializers import ShortLinkSerializer

cache = ShortLinkCache()


class ShortLinkViewSet(viewsets.ModelViewSet):
    serializer_class = ShortLinkSerializer

    def get_queryset(self):
        return ShortLink.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RedirectView(View):
    def get(
        self,
        request,
        code: str,
        *args,
        **kwargs,
    ):
        link_str = cache.get(code)
        if link_str:
            return redirect(link_str)
        link = get_object_or_404(ShortLink, code=code)
        cache.set(code, link.url)
        return redirect(link.url)
