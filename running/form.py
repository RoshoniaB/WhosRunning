from django import forms
from .models import Running


class RunningForm(forms.ModelForm):
    class Meta:
        model = Running
        fields = '__all__'
