import logging

from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin)

from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter

from hive_sbi_api.core.models import Member
from .serializers import MemberSerializer


logger = logging.getLogger('v1')


class MemberViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  GenericViewSet):
    lookup_value_regex = '[^/]+'
    lookup_field = 'account'

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = ['shares', 'bonus_shares', 'estimate_rewarded']
