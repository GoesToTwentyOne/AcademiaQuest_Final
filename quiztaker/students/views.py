from django.shortcuts import render, redirect, reverse, get_object_or_404
from . import forms, models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from quiz import models as QMODEL
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout, authenticate
from quiz.models import Question, Course, Result, QuizHistory
from category.models import CategoryModel
from quiz.forms import RatingForm
from quiz.models import QuizRating
from django.db.models import Avg
from django.views import View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class StudentClickView(View):
    def get(self, request):
        if request.user.is_authenticated:
            categories = CategoryModel.objects.all()
            return render(request, 'student_dashboard.html', {'categories': categories})
        else:
            return render(request, 'user_home.html')


class StudentSignupView(View):
    def get(self, request):
        user_form = forms.StudentUserForm()
        student_form = forms.StudentForm()
        context = {'userForm': user_form, 'studentForm': student_form}
        return render(request, 'signup.html', context)
    
    def post(self, request):
        user_form = forms.StudentUserForm(request.POST)
        student_form = forms.StudentForm(request.POST, request.FILES)
        context = {'userForm': user_form, 'studentForm': student_form}
        
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            
            student_group, _ = Group.objects.get_or_create(name='STUDENT')
            student_group.user_set.add(user)
            
            return redirect('studentlogin')
        
        return render(request, 'signup.html', context)



class StudentLoginView(LoginView):
    template_name = 'studentlogin.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student-dashboard')
        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



@method_decorator(login_required, name='dispatch')
class StudentLogoutView(LogoutView):
    next_page = reverse_lazy('studentlogin')

    def get_next_page(self):
        return self.next_page

    def dispatch(self, request, *args, **kwargs):
        # Override dispatch to set the next_page parameter
        self.next_page = self.get_next_page()
        return super().dispatch(request, *args, **kwargs)
    
    
    

# def student_dashboard_view(request):
#     if request.user.is_authenticated:
#         categories=CategoryModel.objects.all()
#         dict={
#         'total_course':QMODEL.Course.objects.all().count(),
#         'total_question':QMODEL.Question.objects.all().count(),
#         'categories':categories,
#         }
#         return render(request,'student_dashboard.html',context=dict)
#     return redirect('studentlogin')
class StudentDashboardView(TemplateView):
    template_name = 'student_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            categories = CategoryModel.objects.all()
            context['total_course'] = QMODEL.Course.objects.all().count()
            context['total_question'] = QMODEL.Question.objects.all().count()
            context['categories'] = categories
            return context
        else:
            return redirect(reverse('studentlogin'))


class StudentAllExamView(TemplateView):
    template_name = 'student_exam.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            courses = QMODEL.Course.objects.all()
            context['courses'] = courses
            return context
        else:
            return redirect('studentlogin')


# def take_exam_view(request,pk):
#     if request.user.is_authenticated:
#         course=QMODEL.Course.objects.get(id=pk)
#         total_questions=QMODEL.Question.objects.all().filter(course=course).count()
#         questions=QMODEL.Question.objects.all().filter(course=course)
#         total_marks=0
#         for q in questions:
#             total_marks=total_marks + q.marks
#         return render(request,'take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks})
#     return redirect('studentlogin')
class TakeExamView(TemplateView):
    template_name = 'take_exam.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            pk = self.kwargs.get('pk')
            course = QMODEL.Course.objects.get(id=pk)
            questions = QMODEL.Question.objects.filter(course=course)
            total_questions = questions.count()
            total_marks = sum(q.marks for q in questions)
            context['course'] = course
            context['total_questions'] = total_questions
            context['total_marks'] = total_marks
            return context
        else:
            return redirect('studentlogin')




class StartExamView(TemplateView):
    template_name = 'start_exam.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pk = self.kwargs.get('pk')
            course = QMODEL.Course.objects.get(id=pk)
            questions = QMODEL.Question.objects.filter(course=course)
            context = {'course': course, 'questions': questions}
            response = render(request, self.template_name, context)
            response.set_cookie('course_id', course.id)
            return response
        else:
            return redirect('studentlogin')

    def post(self, request, *args, **kwargs):
        pass
    
    


class CalculateMarksView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            total_marks = 0
            course_id = request.COOKIES.get('course_id')
            course = Course.objects.get(id=course_id)
            questions = Question.objects.filter(course=course)
            for i, question in enumerate(questions):
                answer_key = f'answer_{question.id}'
                selected_ans = request.POST.get(answer_key)
                actual_answer = question.answer
                if selected_ans == actual_answer:
                    total_marks += question.marks
            student = QMODEL.Student.objects.get(user_id=request.user.id)
            result = Result()
            result.marks = total_marks
            result.exam = course
            result.student = student
            result.save()
            quiz_history = QuizHistory.objects.create(
                user=request.user,
                course=course,
                score=int(result.marks),
            )
            return redirect('view-result')
        return redirect('studentlogin')

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('studentlogin')) 
   



class ViewResultView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            courses = Course.objects.all()
            return render(request, 'view_result.html', {'courses': courses})
        return redirect('studentlogin')
    


class CheckMarksView(LoginRequiredMixin, View):
    def get(self, request, pk):
        course = QMODEL.Course.objects.get(id=pk)
        student = QMODEL.Student.objects.get(user_id=request.user.id)
        results = QMODEL.Result.objects.filter(exam=course, student=student)
        return render(request, 'check_marks.html', {'results': results})


class StudentMarksTemplateView(LoginRequiredMixin, View):
    def get(self, request):
        courses = QMODEL.Course.objects.all()
        return render(request, 'student_marks.html', {'courses': courses})

class CourseCategoryView(LoginRequiredMixin, View):
    def get(self, request, category_slug=None):
        categories = CategoryModel.objects.all()
        category = get_object_or_404(CategoryModel, slug=category_slug)
        courses = Course.objects.filter(category=category)
        return render(request, 'cat_details.html', {'courses': courses, 'categories': categories, 'category': category})
   

class LeaderboardAgoView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            courses = QMODEL.Course.objects.all()
            return render(request, 'led_ago.html', {'courses': courses})
        return redirect('studentlogin')
    
class LeaderboardView(LoginRequiredMixin, View):
    def get(self, request, course_id, top_n=10):
        course = get_object_or_404(Course, pk=course_id)
        leaderboard = Result.objects.filter(exam=course).order_by('-marks')[:top_n]
        context = {
            'course': course,
            'leaderboard': leaderboard,
        }
        return render(request, 'led_board.html', context)



class QuizHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            quiz_history = QuizHistory.objects.filter(user=user).order_by('-date_taken')
            context = {
                'user': user,
                'quiz_history': quiz_history,
            }
            return render(request, 'quiz_his.html', context)
        return redirect('studentlogin')
  
  
class RateQuizView(View):
    def get(self, request, course_id):
        if request.user.is_authenticated:
            course = Course.objects.get(pk=course_id)
            form = RatingForm()
            context = {
                'course': course,
                'form': form,
            }
            return render(request, 'rate_quiz.html', context)
        else:
            return redirect('studentlogin')
    
    def post(self, request, course_id):
        if request.user.is_authenticated:
            course = Course.objects.get(pk=course_id)
            user = request.user
            form = RatingForm(request.POST)
            if form.is_valid():
                rating_value = form.cleaned_data['rating']
                QuizRating.objects.create(user=user, course=course, rating=rating_value)
                return redirect('quiz_detail', course_id=course_id)
            else:
                context = {
                    'course': course,
                    'form': form,
                }
                return render(request, 'rate_quiz.html', context)
        else:
            return redirect('studentlogin')




class QuizDetailView(View):
    def get(self, request, course_id):
        if request.user.is_authenticated:
            course = Course.objects.get(pk=course_id)
            average_rating = QuizRating.objects.filter(course=course).aggregate(Avg('rating'))['rating__avg']
            context = {
                'course': course,
                'average_rating': average_rating,
            }
            return render(request, 'quiz_detail.html', context)
        else:
            return redirect('studentlogin')

