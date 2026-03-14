from django.db import models

# Create your models here.

class IntrusionLog(models.Model):
    ip_address = models.GenericIPAddressField()
    attack_type = models.CharField(max_length=100)
    path = models.CharField(max_length=255)
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.attack_type}"