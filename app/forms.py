from django import forms
from app.models import account

class accountform(forms.ModelForm):
    class Meta:
        model = account
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }