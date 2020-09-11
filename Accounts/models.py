from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Profile',null = True)
    description = models.CharField(max_length=400, blank = True)
    image = models.ImageField(upload_to = 'profile_photo/',default = 'default.png')
    city = models.CharField(max_length=400, blank = True)



