from django.forms import ModelForm, DateInput
from .models import Deliverables

class DeliverablesForm(ModelForm):
    class Meta:
        model = Deliverables
        fields = ['name','description','due_date']
        widgets = {
            'due_date': DateInput(attrs={'type':'date'})
        }