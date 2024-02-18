from rest_framework import serializers
from .models import Tags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id','tag_name']