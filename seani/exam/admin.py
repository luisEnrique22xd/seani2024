from django.contrib import admin

from .models import Stage

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['stage', 'month','year']
# Register your models here.
