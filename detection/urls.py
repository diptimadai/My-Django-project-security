from django.urls import path
from . import views

urlpatterns = [
    path('', views.detect_intrusion, name='detect_intrusion'),
]