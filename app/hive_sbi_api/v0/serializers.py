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
    lastUpdatedTime = serializers.DateTimeField()
    estimatedMinutesUntilNextUpdate = serializers.IntegerField()

    """
    Line 41 comment #maxSBIVote: pending definition of value source.
    Value must be provided in the file app/hive_sbi_api/v0/views.py
    on line 74. when the value is obtained, remove
    this comment and uncomment the next line (41).
    """
    #maxSBIVote = serializers.FloatField()

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
