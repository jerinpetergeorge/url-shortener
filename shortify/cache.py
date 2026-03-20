from django.core.cache import cache

from . import settings as shortify_settings


class ShortLinkCache:
    namespace = "shortify"

    def get(
        self,
        code: str,
    ):
        return cache.get(f"{self.namespace}:{code}")

    def set(
        self,
        code: str,
        url: str,
        timeout: int = shortify_settings.CACHE_TTL,
    ):
        cache.set(f"{self.namespace}:{code}", url, timeout=timeout)
