from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("vault.urls")),
    path("opinions/", include("opinion.urls")),
    path("tags",include('tags.urls')),
]
