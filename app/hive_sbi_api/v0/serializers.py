from rest_framework import serializers
from rest_framework import serializers

from hive_sbi_api.core.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        ref_name = 'V0 - User data'
        fields = [
            'username',
            'note',
            'shares',
            'bonusShares',
            'balanceRShares',
            'subscribedRShares',
            'curationRShares',
            'delegationRShares',
            'otherRShares',
            'totalRShares',
            'rewardedRShares',
            'commentUpvote',
            'estimateBalanceValue',
            'estimatedNextVote',
            'estimateRewarded',
            'skiplisted',
        ]


class StatusSerializer(serializers.Serializer):
    last_updated_time = serializers.DateTimeField(label="lastUpdatedTime")
    estimated_minutes_until_next_update = serializers.IntegerField(
        label="estimatedMinutesUntilNextUpdate"
    )
    #max_sbi_vote = serializers.FloatField(label="maxSBIVote")

    class Meta:
        ref_name = 'V0 - Status'


class NotFoundSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    error = serializers.CharField()
    status = StatusSerializer(many=False, read_only=True)


class UserSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    data = MemberSerializer(many=False, read_only=True)
    status = StatusSerializer(many=False, read_only=True)

    class Meta:
        ref_name = 'V0 - Response'
