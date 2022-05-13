from django.forms import ModelForm, DateInput
from .models import Actionitems

class ActionitemsForm(ModelForm):
    class Meta:
        model = Actionitems
        fields = '__all__'
        exclude = ["uuid"]
        widgets = {
            'date_created': DateInput(attrs={'type':'date'}),
            'date_assigned': DateInput(attrs={'type':'date'}),
            'expected_completion_date': DateInput(attrs={'type':'date'}),
            'actual_completion_date': DateInput(attrs={'type':'date'}),
            'update_date': DateInput(attrs={'type':'date'})
        }