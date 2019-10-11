from django import forms
from .models import EmployeeInfo

class EmployeeForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = EmployeeInfo
        fields = ('username', 'password', 'name', 'mobile', 'designation')
    
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
        }