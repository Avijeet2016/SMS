from django.urls import path
from .views import std_attendance, StudentAttendance, ResultView, StudentInfoView


urlpatterns = [
    path('attendance/<str:std_cls>/<int:std_roll>', StudentAttendance.as_view(), name='student-attendance'),
    path('result', ResultView.as_view()),
    path('studentinfo', StudentInfoView.as_view()), 
]

