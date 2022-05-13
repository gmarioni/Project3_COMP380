from operator import rshift
from deliverablesApp.models import Deliverables
from django.contrib.auth.models import User
import core.core as corefunc
from .models import Tasks

def createTasks(rjson):
    obj_d = Tasks.objects.create()   
    setattr(obj_d,"uuid",corefunc.generateUUID(Tasks._meta.db_table,obj_d.id))
    for f in Tasks._meta.fields:
        if f.name not in ("id","uuid"):
            if f.name is 'deliverable_id':
                setattr(obj_d,f.name,Deliverables.objects.get(id=rjson[f.name]))
            elif f.name is 'assigned_to':
                setattr(obj_d,f.name,User.objects.get(id=rjson[f.name]))
            else:
                setattr(obj_d,f.name,rjson[f.name])
    obj_d.save()

def updateTasks(obj_d,rjson):
    for f in Tasks._meta.fields:
        if f.name not in ("id","uuid"):
            if f.name is 'deliverable_id':
                setattr(obj_d,f.name,Deliverables.objects.get(id=rjson[f.name]))
            elif f.name is 'assigned_to':
                setattr(obj_d,f.name,User.objects.get(id=rjson[f.name]))
            else:
                setattr(obj_d,f.name,rjson[f.name])
    obj_d.save()
