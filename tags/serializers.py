from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ["id", "name", "children"]

    def get_children(self, obj):
        children = obj.parent_category.all()
        serializer = TagSerializer(children, many=True)
        return serializer.data
