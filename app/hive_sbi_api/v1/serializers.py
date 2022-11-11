from rest_framework import serializers

from hive_sbi_api.core.models import (Member,
                                      Transaction,
                                      Sponsee,
                                      Post,
                                      Vote)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'account',
            'note',
            'shares',
            'bonus_shares',
            'total_shares',
            'total_share_days',
            'avg_share_age',
            'last_comment',
            'last_post',
            'original_enrollment',
            'latest_enrollment',
            'flags',
            'earned_rshares',
            'subscribed_rshares',
            'curation_rshares',
            'delegation_rshares',
            'other_rshares',
            'rewarded_rshares',
            'total_rshares',
            'estimate_rewarded',
            'balance_rshares',
            'upvote_delay',
            'updated_at',
            'first_cycle_at',
            'last_received_vote',
            'blacklisted',
            'hivewatchers',
            'buildawhale',
            'skiplist',
            'pending_balance',
            'next_upvote_estimate',
        ]


class SponseeSerializer(serializers.ModelSerializer):
    account = serializers.CharField(source='account.account')
    class Meta:
        model = Sponsee
        fields = [
            'account',
            'units',
        ]


class TransactionSerializer(serializers.ModelSerializer):
    sponsees = SponseeSerializer(many=True, read_only=True)

    class Meta:
        model = Transaction
        fields = [
            'index',
            'source',
            'memo',
            'account',
            'sponsor',
            'sponsees',
            'shares',
            'vests',
            'timestamp',
            'status',
            'share_type',
        ]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = [
            'voter',
            'weight',
            'rshares',
            'percent',
            'reputation',
            'time',
        ]


class PostSerializer(serializers.ModelSerializer):
    vote_set = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'permlink',
            'title',
            'created',
            'vote_rshares',
            'total_payout_value',
            'author_rewards',
            'total_rshares',
            'vote_set',
        ]
