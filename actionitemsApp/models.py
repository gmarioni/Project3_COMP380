from django.db import models
from django.contrib.auth.models import User
from issuesApp.models import Issues
from core.models import Status

# Create your models here.
class Actionitems(models.Model):
    issue_id = models.ForeignKey(Issues,on_delete=models.SET_NULL,null=True)
    uuid = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    date_assigned = models.DateField(blank=True, null=True)
    assigned_to = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    expected_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    status_id = models.ForeignKey(Status,on_delete=models.SET_NULL,blank=True, null=True)
    status_description = models.TextField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'ACTIONITEMS'

    def __str__(self) -> str:
        return self.uuid