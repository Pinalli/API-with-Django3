#from django.shortcuts import render
from rest_framework import viewsets, generics
from school.models import Course, Student, Registration
from school.serializer import CourseSerializer, StudentSerializer, RegistrationSerializer, ListRegistrationsStudentSerializer, ListStudentsRegistrationSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CoursesViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationViewSet(viewsets.ModelViewSet):
    """Showing all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
class ListRegistrationsStudent(generics.ListAPIView):
    """Listing all registrations of the a student"""
    def get_queryset(self):
       queryset = Registration.objects.filter(student_id=self.kwargs['pk'])               
       return queryset
    serializer_class = ListRegistrationsStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListStudentsRegistration(generics.ListAPIView):    
    """Listing all students enrolled in a course"""
    def get_queryset(self):
       queryset = Registration.objects.filter(course_id=self.kwargs['pk'])               
       return queryset
    serializer_class = ListStudentsRegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

