from django.contrib import admin
from apps.users.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):  
    def full_name(self):
        return self.get_full_name  
        
    list_display = (full_name, 'username', 'email', 'phone', 'gender', 'created_at')
    search_fields = ('first_name', 'details', 'last_name', 'email', 'username', 'phone', 'gender')