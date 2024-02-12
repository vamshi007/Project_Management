from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_ID = models.EmailField()
    location = models.CharField(max_length=100)
    extension_line = models.CharField(max_length=10)




