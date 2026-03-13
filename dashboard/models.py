from django.db import models

# Create your models here.

class DashboardData(models.Model):
    ip_address = models.GenericIPAddressField()
    intrusion_type = models.CharField(max_length=100)
    risk_score = models.IntegerField()
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.intrusion_type}"