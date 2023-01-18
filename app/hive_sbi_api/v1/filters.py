from django_filters import rest_framework as filters

from hive_sbi_api.core.models import (Transaction,
                                      Post,
                                      MaxDailyHivePerMVest)


class TransactionFilter(filters.FilterSet):
    account = filters.CharFilter(
        field_name='account',
        lookup_expr='iexact',
        label='account',
    )

    sponsor = filters.CharFilter(
        field_name='sponsor__account',
        lookup_expr='iexact',
        label='sponsor',
    )

    sponsee = filters.CharFilter(
        field_name='sponsees__account__account',
        lookup_expr='iexact',
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


class PostFilter(filters.FilterSet):
    author = filters.CharFilter(
        field_name='author',
        lookup_expr='iexact',
        label='author',
    )

    class Meta:
        model = Post
        fields = (
            'author',
        )


class MaxDailyHivePerMVestFilter(filters.FilterSet):
    date = filters.DateFilter(
        field_name='timestamp',
        lookup_expr="istartswith",
        label='date',
    )

    start_date = filters.DateFilter(
        field_name='timestamp',
        lookup_expr="gte",
        label='start date',
    )

    end_date = filters.DateFilter(
        field_name='timestamp',
        lookup_expr="lte",
        label='end date',
    )

    class Meta:
        model = MaxDailyHivePerMVest
        fields = (
            'date',
            'start_date',
            'end_date',
        )
