from .models import Deliverables
import core.core as corefunc

def createDeliverable(rjson):
    print(json)
    obj_d = Deliverables.objects.create(
        name=rjson["name"],
        description=rjson["description"],
        due_date=rjson["due_date"]
    )   
    uuid = corefunc.generateUUID(Deliverables._meta.db_table,obj_d.id)
    Deliverables.objects.filter(id=obj_d.id).update(uuid=uuid)

def updateDeliberable(obj_d,rjson):
    for f in Deliverables._meta.fields:
        if f.name not in ("id","uuid"):
            setattr(obj_d,f.name,rjson[f.name])
    obj_d.save()
