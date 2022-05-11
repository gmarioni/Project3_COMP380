from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Priority(models.Model):
    priority = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'PRIORITY'
    
    def __self__(self):
        return self.priority


class Serverity(models.Model):
    serverity = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'SERVERITY'
    
    def __self__(self):
        return self.serverity


class Status(models.Model):
    status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'STATUS'

    def __self__(self):
        return self.status

# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)

#     avatar = models.ImageField(null=True, default="avatar.svg")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
