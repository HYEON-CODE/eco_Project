from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    account = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    
