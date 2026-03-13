from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default='user')  # e.g., 'admin', 'user', etc.
    created_at = models.DateTimeField(auto_now_add=True)
    # Add additional fields as needed, e.g., profile picture, bio, etc.
    
    def __str__(self):
        return self.user.username