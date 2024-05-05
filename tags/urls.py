from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GetAllOpinionsForSingleTag, TagReadOnlyView, AllTagReadOnlyView

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r"", TagReadOnlyView, basename="tags")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("all/", AllTagReadOnlyView.as_view(), name="all-topics"),
    path("opinions/<slug>/", GetAllOpinionsForSingleTag.as_view(), name="all-opinions"),
    path("", include(router.urls)),
]
