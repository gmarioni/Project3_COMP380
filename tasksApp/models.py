from django.db import models

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    deliverable_id = models.IntegerField()
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.IntegerField(blank=True, null=True)
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
    predecessor_task = models.TextField(blank=True, null=True)
    successor_task = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TASKS'