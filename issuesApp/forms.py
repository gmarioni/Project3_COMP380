from django.forms import ModelForm, DateInput
from .models import Issues

class IssuesForm(ModelForm):
    class Meta:
        model = Issues
        fields = '__all__'
        exclude = ["uuid"]
        widgets = {
            'date_raised': DateInput(attrs={'type':'date'}),
            'date_assigned': DateInput(attrs={'type':'date'}),
            'expected_completion_date': DateInput(attrs={'type':'date'}),
            'actual_completion_date': DateInput(attrs={'type':'date'}),
            'update_date': DateInput(attrs={'type':'date'})
        }