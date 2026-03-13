from django.contrib import admin
from .models import DashboardData
# Register your models here.

@admin.register(DashboardData)
class DashboardDataAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'intrusion_type', 'risk_score', 'detected_at')
    list_filter = ('intrusion_type',)
    search_fields = ('ip_address',)