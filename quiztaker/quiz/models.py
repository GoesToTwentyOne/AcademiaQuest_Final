from django.db import models
from students.models import Student
from category.models import CategoryModel
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.
class Course(models.Model):
   course_name = models.CharField(max_length=50,null=False,blank=False)
   slug=models.SlugField(max_length=150,unique=True,null=True)
   question_number = models.PositiveIntegerField(null=False,blank=False)
   total_marks = models.PositiveIntegerField(null=False,blank=False)
   category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
   last_modified_date=models.DateTimeField(auto_now=True)
   average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
   rating_count = models.PositiveIntegerField(default=0)
   def clean(self):
        min_questions = 5
        max_questions = 50
        if self.question_number < min_questions or self.question_number > max_questions:
            raise ValidationError(
                f"A quiz must have between {min_questions} and {max_questions} questions."
            )
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField(null=False,blank=False)
    description=models.CharField(max_length=150,null=True)
    has_time_limit=models.PositiveIntegerField(null=True)
    question=models.CharField(max_length=600,null=False,blank=False)
    a=models.CharField(max_length=200,null=False,blank=False)
    b=models.CharField(max_length=200,null=False,blank=False)
    c=models.CharField(max_length=200,null=True,blank=True)
    d=models.CharField(max_length=200,null=True,blank=True)

    cat = (
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
    ('d', 'd'),

    )
    answer=models.CharField(max_length=200,choices=cat)
    def __str__(self):
        return self.question
    
    
class QuizHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Quiz History for {self.course.course_name}"
    
class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    quiz_history = models.ForeignKey(QuizHistory, on_delete=models.SET_NULL, null=True, blank=True)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student.user.first_name
    
    
    

class QuizRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')))


    def __str__(self):
        return f"{self.user.username}'s Rating for {self.course.course_name}"

