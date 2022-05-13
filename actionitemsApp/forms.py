from django.forms import ModelForm
from .models import Actionitems

class ActionitemsForm(ModelForm):
    class Meta:
        model = Actionitems
        fields = '__all__'
        exclude = ["uuid"]
