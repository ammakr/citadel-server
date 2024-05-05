from rest_framework.viewsets import ModelViewSet
from .serializers import TagSerializer
from .models import Tag


class TagReadOnlyView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(parent=None)
