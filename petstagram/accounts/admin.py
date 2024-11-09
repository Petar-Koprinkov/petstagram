from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from petstagram.accounts.forms import AppUserChangeForm, AppUserCreationForm

UserModel = get_user_model()


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    model = UserModel
    form = AppUserChangeForm
    add_form = AppUserCreationForm

    list_display = ("pk", "email", "is_staff", "is_superuser")
    ordering = ("pk",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ()}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email",  "password1", "password2"),
            },
        ),
    )
