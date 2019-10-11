from django.shortcuts import render, redirect
from .models import TeacherInfo
from .forms import TeacherForm

def delete_teacher(request, teacher_id):
    teacher_obj = TeacherInfo.objects.get(id=teacher_id)
    teacher_obj.delete()
    return redirect('teacher-list')


def edit_teacher(request, teacher_id):
    teacher_obj = TeacherInfo.objects.get(id=teacher_id)
    forms = TeacherForm(instance=teacher_obj)
    if request.method == "POST":
        forms = TeacherForm(request.POST, instance=teacher_obj)
        if forms.is_valid():
            forms.save()
            return redirect('teacher-list')
    context = {
        'forms': forms,
    }
    return render(request, 'teacher/edit_teacher.html', context)


def create_teacher(request):
    forms = TeacherForm()
    if request.method == "POST":
        forms = TeacherForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('teacher-list')

    context = {
        'forms': forms,
    }
    return render(request, 'teacher/create_teacher.html', context)


def teacher_list(request):
    teachers = TeacherInfo.objects.order_by('-id')
    context = {
        'teachers': teachers,
    }
    return render(request, 'teacher/teacher_list.html', context)


