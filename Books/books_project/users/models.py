import imp
from operator import imod
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.


class Users(models.Model):
    username= models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio= models.TextField()

    def __str__(self):
        return str(self.username) 