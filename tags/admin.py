from django.contrib import admin
from .models import Tags


# Register your models here.
@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag_name']