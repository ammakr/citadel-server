from rest_framework import serializers
from .models import Tag


class SimpleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]
        read_only_fields = ["id", "slug"]


class TagSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ["id", "name", "children", "slug"]
        read_only_fields = ["id", "name", "slug"]

    def get_children(self, obj):
        children = obj.parent_tag.all()
        serializer = TagSerializer(children, many=True)
        return serializer.data


class AllTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]
        read_only_fields = ["id", "name", "slug"]
