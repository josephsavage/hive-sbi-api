from rest_framework import routers
from .views import (MemberViewSet,
                    TransactionViewSet,
                    PostViewSet,
                    MaxDailyHivePerMVestViewSet)


router = routers.DefaultRouter()
router.register(r'users', MemberViewSet)
router.register(r'members', MemberViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'posts', PostViewSet)
router.register(r'hive-per-mvest', MaxDailyHivePerMVestViewSet)

api_v1_urlpatterns = router.urls
