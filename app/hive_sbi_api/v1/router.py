from rest_framework import routers
from .views import (MemberViewSet,
                    TransactionViewSet)


router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'transactions', TransactionViewSet)

api_v1_urlpatterns = router.urls
