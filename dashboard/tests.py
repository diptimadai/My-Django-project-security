from django.test import TestCase
from .models import DashboardData

# Create your tests here.

class DashboardTests(TestCase):

    def test_dashboard_data_creation(self):
        data = DashboardData.objects.create(
            ip_address='192.168.1.1',
            intrusion_type='Test Intrusion',
            risk_score=50
        )
        self.assertEqual(data.ip_address, '192.168.1.1')
        self.assertEqual(data.risk_score, 50)