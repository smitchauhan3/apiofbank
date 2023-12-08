from rest_framework import serializers
from .models import *

# DRF(Django RestFramework) provides serializers that allow complex data types, such as Django models, to be easily converted to Python data types (e.g., dictionaries) and vice versa.

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    cus_id = serializers.ReadOnlyField()
    class Meta:
        model = Customer
        fields = '__all__'
        
        def validate_account_number(self, value):
            if Account.objects.filter(account_number=value).exists():
                raise serializers.ValidationError("An account with this account number already exists.")
            return value
            
class EmployeeSerializer(serializers.ModelSerializer):
     class Meta:
         model = Employee
         fields = '__all__'
        