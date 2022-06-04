from django_filters import rest_framework as filters

from hive_sbi_api.core.models import Transaction


class TransactionFilter(filters.FilterSet):
    account = filters.CharFilter(
        field_name='account__account',
        label='account',
    )

    sponsor = filters.CharFilter(
        field_name='sponsor__account',
        label='sponsor',
    )

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
            'share_type',
            'sponsee',
        )
