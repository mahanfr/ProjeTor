from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from .models import Profile, User


class UserConfig(UserAdmin):
    model = User
    search_fields = ('email', 'user_name', 'phone_number')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('-created_at',)
    list_display = ("profile", 'email', 'user_name', 'phone_number',
                    'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    # This is used for creating a new user in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


# Register your models here.
admin.site.register(User, UserConfig)
admin.site.register(Profile)
