from django.contrib import admin
from .models import UserAccount

# Register your models here.
@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "is_active",
    ]