from rest_framework import serializers
from django.utils.text import slugify
from tags.models import Tag
from tags.serializers import SimpleTagSerializer, TagSerializer

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
    user = UserSerializer(read_only=True)
    tag = SimpleTagSerializer()

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
            "tag",
        )
        read_only_fields = [
            "slug",
        ]

    def create(self, validated_data):
        title = validated_data["title"]
        base_slug = slugify(title)
        slug = base_slug
        count = 1
        while Opinion.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{count}"
            count += 1
        validated_data["slug"] = slug
        return super().create(validated_data)
