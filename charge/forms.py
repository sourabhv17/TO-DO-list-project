from django import forms
from .models import User

class new(forms.ModelForm):
    class Meta:
        model = User
        fields = ['task','description']
        widgets= {
            'task':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
        }