from django.shortcuts import render
from detection.models import IntrusionLog  # assuming this model exists in detection app
from firewall.models import BlockedIP     # assuming firewall tracks blocked IPs
# Create your views here.

def dashboard_view(request):
    intrusions = IntrusionLog.objects.order_by('-detected_at')[:50]  # latest 50 intrusions
    blocked_ips = BlockedIP.objects.order_by('-blocked_at')[:50]     # latest 50 blocked IPs

    context = {
        'intrusions': intrusions,
        'blocked_ips': blocked_ips,
    }
    return render(request, 'dashboard/dashboard.html', context)