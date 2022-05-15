from datetime import datetime
from deliverablesApp.models import Deliverables
from issuesApp.models import Issues
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
            elif f.name == 'expected_duration' and len(str(rjson[f.name])) < 1:
                if len(str(rjson["expected_start_date"])) > 0 and len(str(rjson["expected_end_date"])) > 0:
                    setattr(obj,f.name,corefunc.calculateDuration(rjson["expected_start_date"], rjson["expected_end_date"]))
            elif f.name == 'expected_end_date':
                if len(str(rjson["expected_start_date"])) > 0 and len(str(rjson["expected_duration"])) > 0 \
                    and len(str(rjson["expected_end_date"])) < 1:
                    setattr(obj,f.name,corefunc.calculateEndDate(rjson["expected_start_date"], int(rjson["expected_duration"])))
                elif len(str(rjson[f.name])) > 0:
                    setattr(obj,f.name,rjson[f.name])
            else:
                if len(str(rjson[f.name])) > 0:
                    setattr(obj,f.name,rjson[f.name])
                else:
                    setattr(obj,f.name,None)

def getAssociatedIssues(fk_id) -> Issues:
    return Issues.objects.filter(task_id=fk_id)