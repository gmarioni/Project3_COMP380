from django.forms import ModelForm
from .models import Deliverables

class DeliverablesForm(ModelForm):
    class Meta:
        model = Deliverables
        fields = ['name','description','due_date']
