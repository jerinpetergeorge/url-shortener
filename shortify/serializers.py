from rest_framework import serializers

from .models import ShortLink


class ShortLinkSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    short_url = serializers.SerializerMethodField()

    def get_short_url(self, obj: ShortLink):
        request = self.context.get("request")
        return request.build_absolute_uri(f"/{obj.code}/")

    class Meta:
        model = ShortLink
        fields = [
            "id",
            "url",
            "short_url",
            "alias",
            "user",
            "expires_at",
            "created",
            "modified",
        ]
        read_only_fields = [
            "id",
            "user",
            "created",
            "modified",
        ]
