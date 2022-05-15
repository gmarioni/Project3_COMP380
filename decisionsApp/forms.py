from django.forms import DateInput, ModelForm
from .models import Decisions,Notes

class DecisionsForm(ModelForm):
    class Meta:
        model = Decisions
        fields = '__all__'
        exclude = ["uuid"]
        widgets = {
            'date_created': DateInput(attrs={'type':'date'}),
            'date_needed': DateInput(attrs={'type':'date'}),
            'expected_completion_date': DateInput(attrs={'type':'date'}),
            'actual_completion_date': DateInput(attrs={'type':'date'}),
            'update_date': DateInput(attrs={'type':'date'}),
            'date_made': DateInput(attrs={'type':'date'})
        }
    
class DecisionsForm(ModelForm):
    class Meta:
        model = Decisions
        fields = '__all__'
        exclude = ["uuid"]
        widgets = {
            'date_created': DateInput(attrs={'type':'date'}),
            'date_needed': DateInput(attrs={'type':'date'}),
            'expected_completion_date': DateInput(attrs={'type':'date'}),
            'actual_completion_date': DateInput(attrs={'type':'date'}),
            'update_date': DateInput(attrs={'type':'date'}),
            'date_made': DateInput(attrs={'type':'date'})
        }
    