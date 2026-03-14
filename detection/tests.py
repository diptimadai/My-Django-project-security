from django.test import TestCase
from .models import IntrusionLog                    
# Create your tests here.

class IntrusionLogTest(TestCase):

    def test_create_intrusion_log(self):
        intrusion = IntrusionLog.objects.create(
            ip_address="192.168.1.1",
            intrusion_type="Test Attack",
            risk_score=80
        )

        self.assertEqual(intrusion.ip_address, "192.168.1.1")
        self.assertEqual(intrusion.risk_score, 80)