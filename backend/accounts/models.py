from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addresses', db_column='user_id')
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    nation = models.CharField(max_length=100)
    home_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
 
    class Meta:
        db_table = 'address'
 
    def __str__(self):
        return f'{self.full_name} - {self.city}'