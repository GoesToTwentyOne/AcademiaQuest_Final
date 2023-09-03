from django.shortcuts import render,redirect,reverse,get_object_or_404
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from quiz import models as QMODEL
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout,authenticate
from quiz.models import Question,Course,Result,QuizHistory
from category.models import CategoryModel
from quiz.forms import RatingForm
from quiz.models import QuizRating
from django.db.models import Avg


def studentclick_view(request):
    if request.user.is_authenticated:
        categories=CategoryModel.objects.all()
        return HttpResponseRedirect('student-dashboard',{'categories':categories})
    return render(request,'user_home.html')

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'signup.html',context=mydict)

class Student_logIn(LoginView):
    template_name='studentlogin.html'
   
def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student-dashboard') 
    return render(request, 'studentlogin')


@login_required
def student_logout(request):
    logout(request)
    return redirect('studentlogin')  
    
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()






def student_dashboard_view(request):
    categories=CategoryModel.objects.all()
    dict={
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    'categories':categories,
    }
    return render(request,'student_dashboard.html',context=dict)


def student_exam_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student_exam.html',{'courses':courses})


def take_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    total_questions=QMODEL.Question.objects.all().filter(course=course).count()
    questions=QMODEL.Question.objects.all().filter(course=course)
    total_marks=0
    for q in questions:
        total_marks=total_marks + q.marks
    
    return render(request,'take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks})


def start_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    questions=QMODEL.Question.objects.all().filter(course=course)
    if request.method=='POST':
        pass
    response= render(request,'start_exam.html',{'course':course,'questions':questions})
    response.set_cookie('course_id',course.id)
    return response

def calculate_marks_view(request):
    if request.method == 'POST':
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

        return HttpResponseRedirect('view-result')
   






def view_result_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'view_result.html',{'courses':courses})
    


def check_marks_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    student = models.Student.objects.get(user_id=request.user.id)
    results= QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request,'check_marks.html',{'results':results})


def student_marks_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student_marks.html',{'courses':courses})


def Course_cat(request,category_slug=None):
        categories=CategoryModel.objects.all()
        category=get_object_or_404(CategoryModel,slug=category_slug)
        Courses=Course.objects.filter(category=category)
        return render(request,'cat_details.html',{'courses':Courses,'categories':categories})
        
   

def led_board_ago(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'led_ago.html',{'courses':courses})
    
def leaderboard(request, course_id, top_n=10):
    course = Course.objects.get(pk=course_id)
    leaderboard = Result.objects.filter(exam=course).order_by('-marks')[:top_n]
    context = {
        'course': course,
        'leaderboard': leaderboard,
    }
    return render(request, 'led_board.html', context)

def quiz_history(request):
    user = request.user
    quiz_history = QuizHistory.objects.filter(user=user).order_by('-date_taken')
    context = {
        'user': user,
        'quiz_history': quiz_history,
    }
    return render(request, 'quiz_his.html', context)
  
  
  
def rate_quiz(request, course_id):
    course = Course.objects.get(pk=course_id)
    user = request.user
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data['rating']
            QuizRating.objects.create(user=user, course=course, rating=rating_value)
            return redirect('quiz_detail', course_id=course_id)  
    else:
        form = RatingForm()

    context = {
        'course': course,
        'form': form,
    }

    return render(request, 'rate_quiz.html', context)




def quiz_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    average_rating = QuizRating.objects.filter(course=course).aggregate(Avg('rating'))['rating__avg']

    context = {
        'course': course,
        'average_rating': average_rating,
    }

    return render(request, 'quiz_detail.html', context)

