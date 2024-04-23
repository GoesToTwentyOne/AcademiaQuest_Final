from django.urls import path
from students import views

urlpatterns = [
path('student_click/', views.StudentClickView.as_view(),name='user_home'),
path('student_signup/', views.StudentSignupView.as_view(),name='registrations'),
path('student_login/', views.StudentLoginView.as_view(),name='studentlogin'),
path('logout/', views.StudentLogoutView.as_view(), name='logout'),
path('student_dashboard/', views.StudentDashboardView.as_view(),name='student-dashboard'),
path('student_exam/', views.StudentAllExamView.as_view(),name='student-exam'),
path('take_exam/<int:pk>/', views.TakeExamView.as_view(),name='take-exam'),
path('start_exam/<int:pk>/', views.StartExamView.as_view(),name='start-exam'),
path('calculate_marks/', views.CalculateMarksView.as_view(),name='calculate-marks'),
path('view-result/', views.ViewResultView.as_view(),name='view-result'),
path('check_marks/<int:pk>/', views.CheckMarksView.as_view(),name='check-marks'),
path('student_marks/', views.StudentMarksTemplateView.as_view(),name='student-marks'),
path('category/<slug:category_slug>/', views.CourseCategoryView.as_view(), name='category'),
path('led_ago/', views.LeaderboardAgoView.as_view(),name='led_ago'),
path('leaderboard/<int:course_id>/', views.LeaderboardView.as_view(), name='leaderboard'),
path('quiz_history/', views.QuizHistoryView.as_view(), name='quiz_history'),
path('rate_quiz/<int:course_id>/', views.RateQuizView.as_view(), name='rate_quiz'),
path('quiz_detail/<int:course_id>/', views.QuizDetailView.as_view(), name='quiz_detail'),

]