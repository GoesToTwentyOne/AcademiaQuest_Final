# forms.py
from django import forms
from .models import Question

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['answer'] 

class RatingForm(forms.Form):
    rating = forms.ChoiceField(
        choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )