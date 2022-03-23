from rest_framework import serializers

from hive_sbi_api.core.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'account',
            'note',
            'shares',
            'bonus_shares',
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
            'balance_rshares',
            'upvote_delay',
            'updated_at',
            'first_cycle_at',
            'last_received_vote',
            'blacklisted',
            'hivewatchers',
            'buildawhale',
        ]
