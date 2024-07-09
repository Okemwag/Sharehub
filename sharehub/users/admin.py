from .models import CustomUser
from django.contrib import admin

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'is_staff']
    search_fields = ['email', 'username']
    readonly_fields = ['date_joined', 'last_login']


admin.site.register(CustomUser, CustomUserAdmin)