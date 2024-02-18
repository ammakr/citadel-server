from rest_framework_nested import routers
from .views import OpinionByTagViewset

router = routers.DefaultRouter()


router.register(r'(?P<tag_name>\w+)',OpinionByTagViewset,basename='tag_opinion')

urlpatterns = [] + router.urls