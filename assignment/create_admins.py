from django.contrib.auth import get_user_model
from django.core.management import call_command

User = get_user_model()

superusers = [
    {'email': 'abhishek@example.com', 'full_name': 'Abhishek Tripathi',
      'username': 'abhi', 'phone_number': 1234567890, 'pincode': 400078},
    {'email': 'pankaj@example.com', 'full_name': 'Pankaj Verma', 
     'username': 'panku', 'phone_number': 1234567890, 'pincode': 400078},
    {'email': 'adam@example.com', 'full_name': 'Adam Levi', 
     'username': 'adi', 'phone_number': 1234567890, 'pincode': 400079},
]

for user in superusers:
    User.objects.create_superuser(
        email=user['email'],
        full_name=user['full_name'],
        username=user['username'],
        phone_number=user['phone_number'],
        pincode=user['pincode'],
        password='password123',
    )

