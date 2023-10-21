from django.contrib import admin
from django.urls import path, include
from bankapiapp.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),   
    path('accounts/<int:pk>/check_balance/', AccountViewSet.as_view({'get': 'check_balance'}), name='account-check-balance'),
]