from datetime import datetime
from deliverablesApp.models import Deliverables
from django.contrib.auth.models import User
import core.core as corefunc
from .models import Tasks

def createTasks(rjson):
    obj = Tasks.objects.create()   
    setattr(obj,"uuid",corefunc.generateUUID(Tasks._meta.db_table,obj.id))
    setAttributes(obj,rjson)
    obj.save()

def updateTasks(obj,rjson):
    setAttributes(obj,rjson)
    obj.save()

def setAttributes(obj, rjson):
    for f in Tasks._meta.fields:
        if f.name not in ("id","uuid") and f.name in rjson.keys():
            if f.name == 'deliverable_id':
                setattr(obj,f.name,Deliverables.objects.get(id=rjson[f.name]))
            elif f.name == 'assigned_to' and len(str(rjson[f.name])) > 0:
                setattr(obj,f.name,User.objects.get(id=rjson[f.name]))
                if rjson["date_assigned"] == 0:
                    setattr(obj,"date_assigned",datetime.today().strftime("%Y-%m-%d"))
            else:
                if len(str(rjson[f.name])) > 0:
                    setattr(obj,f.name,rjson[f.name])
                else:
                    setattr(obj,f.name,None)