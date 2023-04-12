from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from . import models
from . import forms


class CustomUserAdmin(UserAdmin):
    add_form = forms.UserCreationForm
    form = forms.UserChangeForm
    model = models.User
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("username", "email", "first_name", "last_name", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "email", "first_name", "last_name", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide"),
            "fields": (
                "username", "email", "first_name", "last_name", "password1", "password2",
                "is_staff", "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("username", "email")
    ordering = ("username", "email")


admin.site.register(models.User, CustomUserAdmin)


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    pass


@admin.register(models.Cart)
class CartAdmin(ModelAdmin):
    pass


@admin.register(models.Orders)
class OrdersAdmin(ModelAdmin):
    pass

