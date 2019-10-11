from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import StudentInfo, StudentDetailInfo, StudentClassInfo, Attendance
from .forms import StudentRegistrationForm, StudentSearchForm, StudentEditForm, StudentDetailInfoForm, StudentInfoForm


def student_att_count(request):
    class_name = request.GET.get('class_name', None)
    if class_name:
        std_list =StudentDetailInfo.objects.filter(std_class__class_name=class_name).order_by('roll')
        context = {'std_list': std_list}
    else:
        context = {}
    return render(request, 'student/att_count.html', context)


def create_student(request):
    forms = StudentRegistrationForm()
    if request.method == "POST":
        forms = StudentRegistrationForm(request.POST)
        if forms.is_valid():
            std_name = forms.cleaned_data['name']
            fathers_name = forms.cleaned_data['fathers_name']
            roll = forms.cleaned_data['roll']
            std_age  = forms.cleaned_data['age']
            std_gender = forms.cleaned_data['gender']
            address = forms.cleaned_data['address']
            std_class = forms.cleaned_data['std_class']
            std_shift = forms.cleaned_data['std_shift']
            std_session = forms.cleaned_data['std_session']
            std_section = forms.cleaned_data['std_section']


            std = StudentInfo.objects.create(
                name = std_name,
                fathers_name = fathers_name,
                address = address,
                age = std_age,
                gender = std_gender
            )
            StudentDetailInfo.objects.create(
                student = std,
                roll = roll,
                std_class = std_class,
                std_shift = std_shift,
                std_section = std_section,
                std_session = std_session
            )
            return redirect('student-list')
    
    context = {
        'forms': forms,
    }
    return render(request, 'student/create_student.html', context)


def student_list(request):
    stds = StudentDetailInfo.objects.select_related('student', 'std_class').order_by('-id')
    context = {'stds': stds}
    return render(request, 'student/student_list.html', context)


def classwise_student_list(request, class_name):
    class_name_obj = StudentClassInfo.objects.get(class_name=class_name)
    stds = StudentDetailInfo.objects.filter(std_class=class_name_obj)
    context = {
        'stds': stds,
        'class': class_name,
    }
    return render(request, 'student/classwise_student_list.html', context)


def search_student(request):
    forms = StudentSearchForm()
    std_class = request.GET.get('std_class', None)
    std_roll = request.GET.get('roll', None)
    std_session = request.GET.get('std_session', None)

    if std_class:
        std = StudentDetailInfo.objects.filter(std_class__id=std_class)
        if std_roll:
            std = std.filter(roll=std_roll)
        if std_session:
            std = std.filter(std_session=std_session)
        context = {'forms': forms, 'std': std, }
        return render(request, 'student/search.html', context)

    context = {'forms': forms,}
    return render(request, 'student/search.html', context)


def student_by_name(request, std_name):
    name_obj = StudentInfo.objects.get(name=std_name)
    std = StudentDetailInfo.objects.get(student__name=name_obj)
    context = {'std': std,}
    return render(request, 'student/student_by_name.html', context)

    
def register_student(request):
    form1 = StudentInfoForm(request.POST or None)
    form2 = StudentDetailInfoForm(request.POST or None)

    if request.method == "POST":
        if form1.is_valid() and form2.is_valid():
            std_obj = form1.save()
            std_detail = form2.save(commit=False)
            std_detail.student = std_obj
            std_detail.save()
            return redirect('student-list')

    context = {'form1': form1, 'form2': form2,}
    return render(request, 'student/register_student.html', context)


def edit_student(request, pk):
    student_detail = StudentDetailInfo.objects.get(id=pk)
    student_info = student_detail.student

    form1 = StudentInfoForm(request.POST or None, instance=student_info)
    form2 = StudentDetailInfoForm(request.POST or None, instance=student_detail)

    if request.method == "POST":
        if form1.is_valid() and form2.is_valid():
            std_obj = form1.save()
            std_detail = form2.save(commit=False)
            std_detail.student = std_obj
            std_detail.save()
            return redirect('student-list')

    context = {'form1': form1, 'form2': form2,}
    return render(request, 'student/edit_student.html', context)


def delete_student(request, pk):
    student_detail = StudentDetailInfo.objects.get(pk=pk)
    student_detail.delete()
    return redirect('student-list')
    
    
@api_view()
def std_attendance(request, std_cls, std_roll):
    try:
        Attendance.objects.create_attendance(std_cls, std_roll)
        #std_obj = StudentDetailInfo.objects.get(std_class__class_name=std_cls, roll=std_roll)
        #att_obj = Attendance.objects.create(student=std_obj, status=1)
        return Response({'status': 'success'})
    except Exception as err:
        print(err)
        return Response({'status': 'failed'})


