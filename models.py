# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actionitems(models.Model):
    actionitem_id = models.AutoField(primary_key=True)
    issue_id = models.IntegerField()
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    date_assigned = models.DateField(blank=True, null=True)
    assigned_to = models.IntegerField(blank=True, null=True)
    expected_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    status_description = models.TextField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ACTIONITEMS'


class Decisions(models.Model):
    decision_id = models.AutoField(primary_key=True)
    issue_id = models.IntegerField()
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    serverity = models.IntegerField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    date_needed = models.DateField(blank=True, null=True)
    decision_maker = models.IntegerField(blank=True, null=True)
    expected_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DECISIONS'


class Deliverables(models.Model):
    deliverable_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DELIVERABLES'


class Issues(models.Model):
    issue_id = models.AutoField(primary_key=True)
    task_id = models.IntegerField()
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    serverity = models.IntegerField(blank=True, null=True)
    date_raised = models.DateField(blank=True, null=True)
    date_assigned = models.DateField(blank=True, null=True)
    expected_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    status_description = models.TextField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ISSUES'


class Notes(models.Model):
    notes_id = models.AutoField(primary_key=True)
    notes = models.TextField(blank=True, null=True)
    decision_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NOTES'


class Priority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    priority = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PRIORITY'


class Serverity(models.Model):
    serverity_id = models.AutoField(primary_key=True)
    serverity = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SERVERITY'


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STATUS'


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


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USERS'
