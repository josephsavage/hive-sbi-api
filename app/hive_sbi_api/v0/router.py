from rest_framework import routers
from .views import MemberViewSet


router = routers.DefaultRouter()
router.register(r'users', MemberViewSet)

api_v0_urlpatterns = router.urls
