from django.db import models

from rest_framework.decorators import action
from rest_framework.response import Response

#Create your models here.
class Account(models.Model):
    account_number = models.CharField(max_length=20, primary_key=True, unique=True)
    customers = models.ForeignKey('Customer', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.account_number} {self.customers.first_name} {self.customers.last_name}'
     


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    hire_date = models.DateField(auto_now=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.job_title}'
