from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)

# def has_superuser_permission(request):
#     return request.user.is_active and request.user.is_superuser

# admin.site.has_permission = has_superuser_permission

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['id','email','username','created','updated','restaurant','staff','admin']
    list_filter = ['admin','created']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','firstname','lastname','restaurant')}),
        ('Permissions', {'fields': ('admin','staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','firstname','lastname','restaurant','password', 'password2')}
        ),
    )
    search_fields = ['email','username','firstname','lastname']
    ordering = ['id']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)