from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserCreateForm, UserUpdateForm

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserUpdateForm
    model = CustomUser
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
