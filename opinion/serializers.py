from rest_framework import serializers

from vault.models import UserAccount
from .models import Opinion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("full_name", "username")

    full_name = serializers.SerializerMethodField()

    def get_full_name(self, user: UserAccount):
        return f"{user.first_name} {user.last_name}"


class OpinionSerializer(serializers.ModelSerializer):
    user = UserSerializer()

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
            "user",
        )
