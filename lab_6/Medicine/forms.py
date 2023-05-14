from .models import *
from django.forms import ModelForm, TextInput


class PatientForm(ModelForm):
    class Meta:
        model = Human
        fields = ['name', 'surname', 'reason']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control'
            }),
            'reason': TextInput(attrs={
                'class': 'form-control'
            })
        }
