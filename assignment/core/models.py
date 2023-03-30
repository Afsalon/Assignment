from django.db import models
from django.contrib.auth.models import AbstractUser
from core.managers import CustomUserManager
from django.core.validators import MaxValueValidator
from core.validators import validate_password
    
class User(AbstractUser):
    full_name=models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[validate_password])
    phone_number = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    country = models.CharField(max_length=90)
    pincode = models.IntegerField(validators=[MaxValueValidator(999999)])
    first_name=None
    last_name=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name','username','phone_number','pincode']

    objects=CustomUserManager()

    def __str__(self):
        return self.email