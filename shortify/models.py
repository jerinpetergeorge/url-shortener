from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from shortify.utils import generate_short_code


class ShortLink(TimeStampedModel):
    url = models.URLField(
        max_length=256,
        verbose_name=_("Original URL"),
    )
    code = models.CharField(
        max_length=7,
        unique=True,
        db_index=True,
        default=generate_short_code,
        verbose_name=_("Short Code"),
    )
    alias = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("Alias"),
    )
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="short_links",
        verbose_name=_("User"),
    )
    expires_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Expires At"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Short Link")
        verbose_name_plural = _("Short Links")
