from django.forms import ModelForm
from .models import Decisions

class DecisionsForm(ModelForm):
    class Meta:
        model = Decisions
        fields = '__all__'
        exclude = ["uuid"]