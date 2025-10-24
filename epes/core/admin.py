from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    
    # Fields you can filter by in admin
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Fields to search users by
    search_fields = ('email', 'first_name', 'last_name')
    
    # Ordering of users
    ordering = ('email',)
    
    # Fields shown in the "add user" form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
