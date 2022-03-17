from rest_framework import routers

from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

api_v1_urlpatterns = router.urls
