from django import forms
from .models import StudentInfo, StudentClassInfo, StudentShiftInfo, StudentDetailInfo


class StudentRegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fathers_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    roll = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = forms.ChoiceField(choices=gender_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    std_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    std_shift = forms.ModelChoiceField(queryset=StudentShiftInfo.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    std_session = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    std_section = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))



class StudentSearchForm(forms.Form):
    std_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    roll = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    std_session = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
 

 
class StudentEditForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    roll = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    std_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

    
class StudentDetailInfoForm(forms.ModelForm):
    class Meta:
        model = StudentDetailInfo
        exclude = ('student', )

        widgets = {
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_class': forms.Select(attrs={'class': 'form-control'}),
            'std_shift': forms.Select(attrs={'class': 'form-control'}),
            'std_section': forms.TextInput(attrs={'class': 'form-control'}),
            'std_session': forms.NumberInput(attrs={'class': 'form-control'}),
        }