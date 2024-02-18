from django.contrib import admin
from .models import Opinion

# Register your models here.
@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ['user','title','description','body','slug','created_at','updated_at','tag']
