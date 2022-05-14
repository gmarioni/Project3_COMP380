from django.forms import ModelForm, DateInput
from .models import Tasks,Task_Dependency

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        exclude = ["uuid"]
        widgets = {
            'expected_start_date': DateInput(attrs={'type':'date'}),
            'expected_end_date': DateInput(attrs={'type':'date'}),
            'actual_start_date': DateInput(attrs={'type':'date'}),
            'actual_end_date': DateInput(attrs={'type':'date'})
        }