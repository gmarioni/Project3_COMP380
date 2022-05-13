from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Priority(models.Model):
    priority = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'PRIORITY'
    
    def __str__(self) -> str:
        return self.priority


class Serverity(models.Model):
    serverity = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'SERVERITY'
    
    def __str__(self) -> str:
        return self.serverity

class Impact(models.Model):
    impact = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'IMPACT'
    
    def __str__(self) -> str:
        return self.impact


class Status(models.Model):
    status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'STATUS'

    def __str__(self) -> str:
        return self.status
