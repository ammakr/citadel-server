from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "hello"})


urlpatterns = [
    path("", HelloWorld.as_view()),
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("vault.urls")),
    path("opinions/", include("opinion.urls")),
    path("tags/", include("tags.urls")),
]
