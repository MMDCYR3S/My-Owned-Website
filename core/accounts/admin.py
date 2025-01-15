from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# Custom user admin panel
@admin.register(User)
class CustomUserAdminPanel(UserAdmin):
    """ Admin panel:
        Create custom admin panel for User model. It gets User as
        a model and then, Set some fields for permissions and important
        information.
        It also adds fieldsets for creating new users.
    """
    model = User
    list_display = ("email", "is_active", "is_staff", "is_superuser")
    list_filter = ("email", "is_active")
    search_fields = ("email", )
    ordering = ("email", )

    fieldsets = (
        ('Authentication',{
            "fields" : ("email", "password"),
        }),
        ('Permissions',{
            "fields" : ("is_active", "is_staff", "is_superuser"),
        }),
        ('Groups Permissions',{
            "fields" : ("groups", "user_permissions"),
        }),
        ('Important Dates',{
            "fields" : ("last_login",),
        }),
    )
    add_fieldsets = (
        ("Authentication",{
            'classes' : ("wide",),
            "fields" : ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

# Profile admin panel
@admin.register(Profile)
class ProfileAdminPanel(admin.ModelAdmin):
    """ Profile admin panel:
        An admin panel for profile which has list display and
        list filter and some other things.
    """
    list_display = ("user", "first_name", "last_name", "job", "created_date")
    list_filter = ("first_name", "last_name")
    search_fields = ("user",)
    ordering = ("first_name", )
