from rest_framework import serializers
from .models import Accounts

class AccountsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Accounts
        fields= [
            'id', 'owner', 'created', 'updated', 'username', 'body', 'image',
        ]