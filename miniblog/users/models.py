from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    language = models.CharField(max_length=30, 
        choices=[
            ('en', ('English')),
            ('es', ('Español')),
        ],
        
    )