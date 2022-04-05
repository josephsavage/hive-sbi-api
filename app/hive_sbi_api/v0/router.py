from rest_framework import routers
from .views import UserInfoHiveViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'getUserInfoHive/?', UserInfoHiveViewSet)

api_v0_urlpatterns = router.urls
