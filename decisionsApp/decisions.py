from datetime import datetime
from issuesApp.models import Issues
from django.contrib.auth.models import User
from core.models import Impact, Status, Priority
import core.core as corefunc
from .models import Decisions

def createIssues(rjson):
    obj = Decisions.objects.create()
    print(rjson)
    setattr(obj,"uuid",corefunc.generateUUID(Decisions._meta.db_table,obj.id))
    setattr(obj,"date_raised",datetime.today().strftime("%Y-%m-%d"))
    setAttributes(obj,rjson)
    obj.save()

def updateIssues(obj,rjson):
    setAttributes(obj, rjson)
    obj.save()

def setAttributes(obj, rjson):
    for f in Decisions._meta.fields:
        if f.name not in ("id","uuid","date_assigned","date_raised","update_date") and \
            f.name in rjson.keys():
            if f.name == 'issue_id':
                setattr(obj,f.name,Issues.objects.get(id=rjson[f.name]))
            elif f.name == 'assigned_to' and len(str(rjson[f.name])) > 0:
                setattr(obj,f.name,User.objects.get(id=rjson[f.name]))
                if rjson["date_assigned"] == 0:
                    setattr(obj,"date_assigned",datetime.today().strftime("%Y-%m-%d"))
            elif f.name == 'impact_id' and len(str(rjson[f.name])) > 0:
                setattr(obj,f.name,Impact.objects.get(id=rjson[f.name]))
            elif f.name == 'status_id' and len(str(rjson[f.name])) > 0:
                setattr(obj,f.name,Status.objects.get(id=rjson[f.name]))
            elif f.name == 'priority_id' and len(str(rjson[f.name])) > 0:
                setattr(obj,f.name,Priority.objects.get(id=rjson[f.name]))
            elif f.name == 'status_description':
                if getattr(obj,f.name) is not None or len(str(rjson[f.name])) != 0:
                    if str(getattr(obj,f.name)) != str(rjson[f.name]):
                        setattr(obj,'update_date',datetime.today().strftime("%Y-%m-%d"))
                    setattr(obj,f.name,rjson[f.name])
            else:
                if len(str(rjson[f.name])) > 0:
                    setattr(obj,f.name,rjson[f.name])
                else:
                    setattr(obj,f.name,None)
