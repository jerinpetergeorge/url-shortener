from django.conf import settings

CONF = getattr(settings, "SHORTIFY_SETTINGS", {})

DEFAULT_BASE_URL = "https://shortify.example.com"
DEFAULT_CODE_LENGTH = 6
DEFAULT_CACHE_TTL = 60 * 60  # 1 hour

BASE_URL = CONF.get("BASE_URL", DEFAULT_BASE_URL)
CODE_LENGTH = CONF.get("CODE_LENGTH", DEFAULT_CODE_LENGTH)
CACHE_TTL = CONF.get("CACHE_TTL", DEFAULT_CACHE_TTL)
