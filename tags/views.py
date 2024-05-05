from rest_framework.mixins import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from opinion.models import Opinion
from opinion.serializers import OpinionSerializer
from .serializers import TagSerializer, AllTagsSerializer
from .models import Tag


class TagReadOnlyView(ModelViewSet):
    serializer_class = TagSerializer
    lookup_field = "slug"

    def get_queryset(self):
        if self.action == "list":
            return Tag.objects.filter(parent=None)
        return Tag.objects.all()


class AllTagReadOnlyView(APIView):
    def get(self, request):
        topics = Tag.objects.all()
        serializer = AllTagsSerializer(topics, many=True)
        return Response(serializer.data)


class GetAllOpinionsForSingleTag(APIView):
    def get(self, request, *args, **kwargs):
        try:
            tag_slug = kwargs["slug"]
            tag = Tag.objects.get(slug=tag_slug)  # Retrieve the tag based on slug
            posts = Opinion.objects.filter(tag=tag)
            serializer = OpinionSerializer(
                posts, many=True, context={"request": request}
            )
            # Retrieve all posts linked to the tag
            # Serialize the posts if needed
            # post_serializer = PostSerializer(posts, many=True)
            # return Response(post_serializer.data)
            # Or you can return data directly
            return Response(serializer.data)
        except Tag.DoesNotExist:
            return Response(
                {"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND
            )
