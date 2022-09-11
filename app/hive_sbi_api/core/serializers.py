from rest_framework import serializers

from hive_sbi_api.sbi.models import SBITransaction


class SBITransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SBITransaction
        fields = '__all__'
