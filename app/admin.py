from django.contrib import admin
from app.models import account

# Register your models here.

class accountadmin(admin.ModelAdmin):
    account_details = ['username','password']


admin.site.register(account,accountadmin)