from django.contrib import admin
from .models import Tag


class TagsAdmin(admin.ModelAdmin):
    fields = ["name", "parent"]
    list_display = ["name", "parent"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by("parent_id", "id")
        return queryset


admin.site.register(Tag, TagsAdmin)
