from django.contrib import admin
from .models import StudentInfo, StudentClassInfo, StudentDetailInfo, StudentShiftInfo, Attendance, Result


class StudentDetailInfoAdmin(admin.ModelAdmin):
    list_display = ['student', 'roll', 'std_class']
    

admin.site.register(StudentInfo)
admin.site.register(StudentClassInfo)
admin.site.register(StudentDetailInfo, StudentDetailInfoAdmin)
admin.site.register(StudentShiftInfo)
admin.site.register(Attendance)
admin.site.register(Result)