from .models import Tasks
import core.core as corefunc

def createTasks(rjson):
    obj_d = Tasks.objects.create()   
    setattr(obj_d,"uuid",corefunc.generateUUID(Tasks._meta.db_table,obj_d.id))
    for f in Tasks._meta.fields:
        if f.name not in ("id","uuid"):
            setattr(obj_d,f.name,rjson[f.name])
    obj_d.save()

def updateTasks(obj_d,rjson):
    for f in Tasks._meta.fields:
        if f.name not in ("id","uuid"):
            setattr(obj_d,f.name,rjson[f.name])
    obj_d.save()
