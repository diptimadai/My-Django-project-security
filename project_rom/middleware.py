from django.http import HttpResponseForbidden
from django.utils import timezone
from datetime import timedelta

from detection.models import IntrusionLog
from firewall.models import BlockedIP


class SecurityMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip = self.get_client_ip(request)

        # check if IP is blocked
        blocked = BlockedIP.objects.filter(ip_address=ip).first()

        if blocked and blocked.is_blocked():
            return HttpResponseForbidden("Your IP is temporarily blocked.")

        # simple suspicious detection example
        if "admin" in request.path or "login" in request.path:

            IntrusionLog.objects.create(
                ip_address=ip,
                attack_type="Suspicious access",
                path=request.path
            )

        response = self.get_response(request)

        return response


    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        return ip