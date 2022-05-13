from django.forms import ModelForm
from .models import Issues

class IssuesForm(ModelForm):
    class Meta:
        model = Issues
        fields = '__all__'
        exclude = ["uuid"]