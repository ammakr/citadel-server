from djoser.serializers import UserSerializer, UserCreateSerializer
from .models import UserAccount
from django.utils.text import slugify


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = UserAccount
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "is_active",
            # "is_staff",
            # "is_superuser",
        )
