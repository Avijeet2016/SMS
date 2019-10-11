from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from student.models import Attendance
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import ResultSerializer, StudentInfoSerializer
from student.models import Result, StudentInfo



class StudentInfoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        student = StudentInfo.objects.all()
        std_serializer = StudentInfoSerializer(student, many=True)
        return Response({'status': std_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentInfoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save() 
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        return Response({'status': serializer.errors }, status=status.HTTP_400_BAD_REQUEST) 



@api_view()
def std_attendance(request, std_cls, std_roll):
    try:
        Attendance.objects.create_attendance(std_cls, std_roll)
        #std_obj = StudentDetailInfo.objects.get(std_class__class_name=std_cls, roll=std_roll)
        #att_obj = Attendance.objects.create(student=std_obj, status=1)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST) 

    

class StudentAttendance(APIView):
    def get(self, request, std_cls, std_roll):
        try:
            Attendance.objects.create_attendance(std_cls, std_roll)
            #std_obj = StudentDetailInfo.objects.get(std_class__class_name=std_cls, roll=std_roll)
            #att_obj = Attendance.objects.create(student=std_obj, status=1)
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST) 



class ResultView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ResultSerializer(data=request.data)

        if serializer.is_valid():
            board = serializer.validated_data['board']
            roll = serializer.validated_data['roll']
            result_obj = Result.objects.get(board=board, roll=roll)
            return Response({'Result': result_obj.gpa}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

           