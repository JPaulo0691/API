from rest_framework import viewsets
import accounts
from accounts.api import serializers
from accounts import models

class AccountsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AccountsSerializer
    queryset = models.UserSetup.objects.all()
    
    
    