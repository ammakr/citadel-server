from rest_framework.mixins import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import TagSerializer, AllTagsSerializer
from .models import Tag


class TagReadOnlyView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(parent=None)


class AllTagReadOnlyView(APIView):
    def get(self, request):
        topics = Tag.objects.all()
        serializer = AllTagsSerializer(topics, many=True)
        return Response(serializer.data)
