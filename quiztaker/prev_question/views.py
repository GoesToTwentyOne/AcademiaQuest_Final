
from django.shortcuts import render, redirect
from . import forms
from prev_question.models import Prev_Questions
from django.views import View

# Create your views here.
from django.views import View

class PreviousQuestionView(View):
    def get(self, request):
        if request.user.is_authenticated:
            prev_form = forms.Prev_questions_Form()
            context = {'Prev_questions_Form': prev_form}
            return render(request, 'prev_view.html', context)
        else:
            return redirect('studentlogin') 
        
    def post(self, request):
        if request.user.is_authenticated:
            prev_form = forms.Prev_questions_Form(request.POST, request.FILES)
            context = {'Prev_questions_Form': prev_form}
            if prev_form.is_valid():
                prev_form.save()
                return redirect('Previous_Question_show') 
            return render(request, 'prev_view.html', context)
        else:
            return redirect('studentlogin') 


class PreviousQuestionShowView(View):
    def get(self, request):
        prev_questions = Prev_Questions.objects.all()
        context = {'prev_questions': prev_questions}
        return render(request, 'prev_quesiton_show.html', context)