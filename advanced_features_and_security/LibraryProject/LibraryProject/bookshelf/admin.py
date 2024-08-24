# bookshelf/admin.py

from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    # Define the fieldsets to display in the user form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # Define the add_fieldsets to display in the user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    # Define the list display fields
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    # Define the search fields
    search_fields = ('email', 'username')
    # Define the ordering fields
    ordering = ('email',)

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')