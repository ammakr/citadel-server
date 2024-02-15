from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status

from opinion.permissions import IsOwner
from .models import Opinion
from .serializers import OpinionSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


class OpinionListCreateView(ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    lookup_field = "slug"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            # Allow unauthenticated users to list and retrieve
            return [permissions.AllowAny()]
        elif self.action == "create":
            # Allow only authenticated users to create
            return [permissions.IsAuthenticated()]
        else:
            # Allow only the owner to edit, update, or delete
            return [IsOwner()]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(detail=False, url_path="@(?P<username>[\w.@+-]+)")
    def by_user(self, request, username=None):
        user_opinions = Opinion.objects.filter(user__username=username)
        serializer = self.get_serializer(user_opinions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
