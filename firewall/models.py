from django.db import models
from django.utils import timezone

# Create your models here.

class BlockedIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    blocked_at = models.DateTimeField(auto_now_add=True)
    unblock_time = models.DateTimeField()

    def is_blocked(self):
        return timezone.now() < self.unblock_time

    def __str__(self):
        return self.ip_address