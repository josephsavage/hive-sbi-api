from rest_framework import serializers
from rest_framework import serializers

from hive_sbi_api.core.models import Member


class UserInfoHiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            '_id',
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
    lastUpdatedTime = serializers.DateTimeField()
    estimatedMinutesUntilNextUpdate = serializers.IntegerField()
    maxSBIVote = serializers.FloatField()


class NotFoundSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    error = serializers.CharField()
    status = StatusSerializer(many=False, read_only=True)


class UserSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    data = UserInfoHiveSerializer(many=False, read_only=True)
    status = StatusSerializer(many=False, read_only=True)
