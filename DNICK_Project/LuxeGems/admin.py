from django.contrib import admin

from LuxeGems.models import Jewelry, Registry, Login, Payment


# Register your models here.

class JewelryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    def has_view_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
admin.site.register(Jewelry, JewelryAdmin)
class RegistryAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

admin.site.register(Registry, RegistryAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display = ("username",)

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

admin.site.register(Login, LoginAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("city","sum_price",)

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

admin.site.register(Payment, PaymentAdmin)
