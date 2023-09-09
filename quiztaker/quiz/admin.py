from django.contrib import admin
from quiz.models import Course,Question,Result,QuizHistory

# Register your models here.
# admin.site.register(Question)
admin.site.register(Result)
admin.site.register(QuizHistory)
# admin.site.register(Course)

class QuestionAdmin(admin.ModelAdmin):
    list_display=['question','course',]
admin.site.register(Question,QuestionAdmin)
class QuizModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['course_name',]}
admin.site.register(Course, QuizModelAdmin)
