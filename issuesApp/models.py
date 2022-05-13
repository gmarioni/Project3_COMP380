from django.db import models
from tasksApp.models import Tasks
from core.models import Serverity, Status, Priority
from django.contrib.auth.models import User

# Create your models here.
class Issues(models.Model):
    task_id = models.ForeignKey(Tasks,on_delete=models.SET_NULL,null=True)
    uuid = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    priority_id = models.ForeignKey(Priority, on_delete=models.SET_NULL,blank=True,null=True)
    serverity_id = models.ForeignKey(Serverity,on_delete=models.SET_NULL,blank=True,null=True)
    date_raised = models.DateField(blank=True, null=True)
    date_assigned = models.DateField(blank=True, null=True)
    expected_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    status_id = models.ForeignKey(Status, on_delete=models.SET_NULL,blank=True,null=True)
    status_description = models.TextField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'ISSUES'
    
    def __str__(self) -> str:
        return self.uuid