# from django.db import models

# class IntrusionLog(models.Model):
#     ip_address = models.GenericIPAddressField()
#     intrusion_type = models.CharField(max_length=100)  # unified name
#     path = models.CharField(max_length=255)
#     risk_score = models.FloatField()
#     detected_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.ip_address} - {self.intrusion_type} - {self.risk_score}"

# in the above code i am basicallly storin the same concept twice:
# which cause
#    SQL injection (attack_type and intrusion_type) which create redundancy, inconsistency and may be there bugs later seen in the logic




from django.db import models

class IntrusionLog(models.Model):
    ip_address = models.GenericIPAddressField()
    intrusion_type = models.CharField(max_length=100)  # unified name
    path = models.CharField(max_length=255)
    risk_score = models.FloatField()
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.intrusion_type} - {self.risk_score}"