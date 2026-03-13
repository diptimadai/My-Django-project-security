from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class AccountsTest(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='test123')
        self.assertEqual(user.username, 'testuser')