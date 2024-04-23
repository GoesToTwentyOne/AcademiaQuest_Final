from django import forms
from prev_question.models import Prev_Questions
class Prev_questions_Form(forms.ModelForm):
    class Meta:
        model=Prev_Questions
        fields=['Semester','LT','previous_question']