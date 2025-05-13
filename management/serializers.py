from rest_framework import serializers
from .models import FinanceRecord
from authentication.serializers import OrganizationSmallSerializer, UserSerializer, OrganizationSerializer
from authentication.models import CustomUser, Organization


class FinanceRecordSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(), required=False)

    class Meta:
        model = FinanceRecord
        fields = ['id', 'organization', 'transaction_type',
                  'amount', 'remarks', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        # Get the organization
        organization = validated_data['organization']

        # Check if transaction is RECEIVED and organization is RECEIVABLE
        if (validated_data['transaction_type'] == 'RECEIVED' and
                organization.transaction_type == 'RECEIVABLE'):
            # Reduce the amount from organization's balance
            organization.balance -= validated_data['amount']
            organization.save()
        elif (validated_data['transaction_type'] == 'PAID' and
              organization.transaction_type == 'PAYABLE'):
            # Reduce the amount from organization's balance
            organization.balance -= validated_data['amount']
            organization.save()

        # Create the finance record
        return super().create(validated_data)


class FinanceRecordListSerializer(serializers.ModelSerializer):
    organization = OrganizationSmallSerializer()

    class Meta:
        model = FinanceRecord
        fields = ['id', 'organization', 'transaction_type',
                  'amount', 'remarks', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
