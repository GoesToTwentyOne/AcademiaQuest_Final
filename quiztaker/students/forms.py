from django import forms
from django.contrib.auth.models import User
from students.models import Student
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'email', 'username', 'password','is_staff']

        widgets = {
        'password': forms.PasswordInput()
        }
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['address','mobile','profile_pic']