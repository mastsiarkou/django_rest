from django.contrib import admin
from .models import Timer

@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
	list_display = ('name', 'datetime')