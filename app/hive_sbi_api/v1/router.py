from rest_framework import routers
from .views import MemberViewSet


router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)

api_v1_urlpatterns = router.urls
