from django.db import models
from django.db.models.fields import CharField, TextField, DateTimeField
from django.utils import timezone
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.urls.base import reverse

# Create your models here.
class Createpost(models.Model):
    title=CharField(max_length=100)
    content=TextField()
    date_posted=DateTimeField(default=timezone.now)
    author=ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# this function is used to redirect the page after the creating the post successfully
    def get_absolute_url(self):
        return reverse('user:home')
    