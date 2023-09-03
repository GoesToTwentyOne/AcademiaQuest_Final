from django.urls import path
from students import views
from students.views import Student_logIn
from django.contrib.auth.views import LoginView

urlpatterns = [
path('studentclick', views.studentclick_view,name='user_home'),
path('studentlogin', Student_logIn.as_view(),name='studentlogin'),
path('login/',views.student_login,name="login"),
path('logout/',views.student_logout,name="logout"),
path('studentsignup', views.student_signup_view,name='registrations'),
path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
path('category/<slug:category_slug>/', views.Course_cat, name='products_by_category'),
path('student-exam', views.student_exam_view,name='student-exam'),
path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),
path('quiz_history/', views.quiz_history, name='quiz_history'),
path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
path('view-result', views.view_result_view,name='view-result'),
path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
path('student-marks', views.student_marks_view,name='student-marks'),
path('led_ago', views.led_board_ago,name='led_ago'),
path('leaderboard/<int:course_id>/', views.leaderboard, name='leaderboard'),
 path('rate_quiz/<int:course_id>/', views.rate_quiz, name='rate_quiz'),
 path('quiz_detail/<int:course_id>/', views.quiz_detail, name='quiz_detail'),

]