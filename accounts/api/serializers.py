from rest_framework import serializers
from accounts import models

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserSetup
        fields = '__all__'
