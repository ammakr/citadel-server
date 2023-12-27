from rest_framework import serializers
from .models import Opinion


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = (
            "id",
            "title",
            "description",
            "body",
            "slug",
            "created_at",
            "updated_at",
        )
