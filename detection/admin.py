from django.contrib import admin
from .models import IntrusionLog
# Register your models here.

@admin.register(IntrusionLog)
class IntrusionLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'intrusion_type', 'risk_score', 'detected_at')
    search_fields = ('ip_address', 'intrusion_type')
    list_filter = ('intrusion_type', 'detected_at')