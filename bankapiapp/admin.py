from django.contrib import admin
from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ('customers', 'account_number', 'balance')
    search_fields = ('name',)
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'email')
    list_filter = ('customer_id',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job_title', 'salary')
    list_filter = ('job_title',)


# Register your models here.
admin.site.register(Account, AccountAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)