from django.db import models
from django.contrib.auth.models import User
from core.models import Priority, Impact, Status
from issuesApp.models import Issues

# Create your models here.
class Decisions(models.Model):
    issue_id = models.ForeignKey(Issues, on_delete=models.SET_NULL,null=True)
    uuid = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    priority_id = models.ForeignKey(Priority, on_delete=models.SET_NULL, blank=True, null=True)
    impact_id = models.ForeignKey(Impact, on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    date_needed = models.DateField(blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_made = models.DateField(blank=True, null=True)
    expected_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    status_id = models.ForeignKey(Status,on_delete=models.SET_NULL,blank=True, null=True)
    status_description = models.TextField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'DECISIONS'

    def __str__(self) -> str:
        return self.uuid

class Notes(models.Model):
    notes = models.TextField(blank=True, null=True)
    decision_id = models.ForeignKey(Decisions, on_delete=models.SET_NULL,blank=True, null=True)

    class Meta:
        db_table = 'NOTES'
    
    def __str__(self) -> str:
        return self.notes