import logging

from django_filters import rest_framework as filters
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin)

from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404

from hive_sbi_api.core.models import (Member,
                                      Transaction)
from .serializers import (MemberSerializer,
                          TransactionSerializer)

from .filters import TransactionFilter


logger = logging.getLogger('v1')


class MemberViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  GenericViewSet):
    lookup_value_regex = '[^/]+'
    lookup_field = 'account'

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = [
        'total_shares',
        'shares',
        'bonus_shares',
        'estimate_rewarded',
        'pending_balance',
        'next_upvote_estimate',
        'total_rshares',]

    def get_object(self):
        """
        Returns the object the view is displaying.
        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg].lower()}

        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


class TransactionViewSet(ListModelMixin,
                         RetrieveModelMixin,
                         GenericViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'index'

    filter_backends = [
        filters.DjangoFilterBackend,
    ]

    filterset_class = TransactionFilter
