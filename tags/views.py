from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from .serializers import TagSerializer
from .models import Tags
from opinion.serializers import OpinionSerializer
from opinion.models import Opinion

# Create your views here.
class TagViewsets(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tags.objects.all()

class OpinionByTagViewset(ModelViewSet):
    serializer_class = OpinionSerializer

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        tag = get_object_or_404(Tags,tag_name=tag_name)
        return Opinion.objects.filter(tag=tag)