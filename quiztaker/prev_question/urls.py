from django.urls import path
from prev_question import views

urlpatterns = [
    path('upload/', views.PreviousQuestionView.as_view(),name='Previous_Question_upload'),
    path('show/', views.PreviousQuestionShowView.as_view(),name='Previous_Question_show'),
]