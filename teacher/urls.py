from django.urls import path
from .views import create_teacher, teacher_list, edit_teacher, delete_teacher


urlpatterns = [
    path('create', create_teacher, name='create-teacher'),
    path('list', teacher_list, name='teacher-list'),
    path('edit/<int:teacher_id>', edit_teacher, name='edit-teacher'),
    path('delete/<int:teacher_id>', delete_teacher, name='delete-teacher'),
]
 