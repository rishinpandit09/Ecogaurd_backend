# Register your models here.

# monitoring/admin.py

from django.contrib.gis import admin
from .models import MonitoringStation, Alert


@admin.register(MonitoringStation)
class MonitoringStationAdmin(admin.GISModelAdmin):
    list_display = ('name', 'location', 'description', 'alert_type','country')  # Include `alert_type`
    list_filter = ('alert_type',)  # Add filter for alert type


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date', 'alert_type')
