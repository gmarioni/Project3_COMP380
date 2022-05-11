from pyexpat import model
from django.db import models

# Create your models here.
class Deliverables(models.Model):
    uuid = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'DELIVERABLES'

    def __str__(self) -> str:
        return self.uuid