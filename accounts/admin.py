from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display= [
        "email",
        "first_name",
        "last_name",
        "company",
        "is_superuser",
    ]
    
    # base fields
    fieldsets = (
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('first_name', 'last_name', 'email', 'company',)
        })
    )
    
    # extra fields
    add_fieldsets = (
        ('Additional info', {
            'fields': ('first_name', 'last_name', 'email', 'company', 'username',)
        }),
    )
    ordering = ('email',)
    
admin.site.register(CustomUser, CustomUserAdmin)