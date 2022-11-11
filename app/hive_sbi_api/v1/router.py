from rest_framework import routers
from .views import (MemberViewSet,
                    TransactionViewSet,
                    PostViewSet)


router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'posts', PostViewSet)

api_v1_urlpatterns = router.urls
