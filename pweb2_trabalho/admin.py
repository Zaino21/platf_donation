from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cargo', 'setor')}), 
    )
    list_display = ('username', 'email', 'cargo', 'setor', 'is_staff')
