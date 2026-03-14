from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import IntrusionLog
from firewall.utils import block_ip_if_needed


def detect_intrusion(request):
    ip = request.META.get('REMOTE_ADDR')

    intrusion_type = "Suspicious Request"
    risk_score = 85  # simulated risk score

    intrusion = IntrusionLog.objects.create(
        ip_address=ip,
        intrusion_type=intrusion_type,
        risk_score=risk_score
    )

    # send to firewall
    block_ip_if_needed(ip, risk_score)

    return JsonResponse({
        "message": "Intrusion detected",
        "ip": ip,
        "risk_score": risk_score
    })