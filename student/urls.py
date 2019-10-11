from django.urls import path
from .views import *


urlpatterns = [
    path('create', create_student, name='create-student'),
    path('list', student_list, name='student-list'),
    path('class/<str:class_name>', classwise_student_list, name='classwise-student-list'),
    path('search', search_student, name='search-student'),
    path('name/<str:std_name>', student_by_name, name='student-name'),
    path('edit/<pk>', edit_student, name='edit-student'),
    path('register', register_student, name='register-student'),
    path('delete/<pk>', delete_student, name='delete-student'),
    path('api/attendance/<str:std_cls>/<int:std_roll>', std_attendance, name='student-attendance'),
    path('att_count', student_att_count, name='student-att-count'),
]
