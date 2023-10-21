from django.shortcuts import render
from rest_framework import viewsets
from bankapiapp.models import *
from bankapiapp.serializers import *

from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    # /bankapiapp/{pk_id}/check_balance/
    @action(detail=True, methods=['get'])
    def check_balance(self, request, pk=None):
        account = self.get_object()
        return Response({'balance': account.balance})
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class EmployeeViewSet(viewsets.ModelViewSet):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer
    
