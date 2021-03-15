from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User

# Create your models here.
class ProfileImage(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics',null=True)
    
    def __str__(self):
        # returning username form the from the profile image module
        return f'{self.user.username} ProfileImage'