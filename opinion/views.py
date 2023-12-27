from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from opinion.permissions import IsOwner
from .models import Opinion
from .serializers import OpinionSerializer


class OpinionListCreateView(ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer

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
