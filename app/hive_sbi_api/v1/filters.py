from django_filters import rest_framework as filters

from hive_sbi_api.core.models import Transaction


class TransactionFilter(filters.FilterSet):
    sponsee = filters.CharFilter(
        field_name='sponsees__account__account',
        label='sponsee',
    )

    class Meta:
        model = Transaction
        fields = (
            'source',
            'account',
            'sponsor',
            'status',
            'status',
            'share_type',
            'sponsee',
        )
