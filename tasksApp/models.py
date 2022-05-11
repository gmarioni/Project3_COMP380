from django.db import models
from deliverablesApp.models import Deliverables
#from core.models import User
from django.contrib.auth.models import User

class Tasks(models.Model):
    deliverable_id = models.ForeignKey(Deliverables, on_delete=models.SET_NULL, null=True)
    uuid = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    expected_start_date = models.DateField(blank=True, null=True)
    expected_end_date = models.DateField(blank=True, null=True)
    expected_duration = models.IntegerField(blank=True, null=True)
    expected_effort = models.IntegerField(blank=True, null=True)
    actual_start_date = models.DateField(blank=True, null=True)
    actual_end_date = models.DateField(blank=True, null=True)
    actual_duration = models.IntegerField(blank=True, null=True)
    effort_completed = models.DateField(blank=True, null=True)
    actual_effort = models.DateField(blank=True, null=True)
    percent_complete = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'TASKS'