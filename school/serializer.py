from rest_framework import serializers
from school.models import Course, Student, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'cpf', 'birthday']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Course
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration        
        exclude = []

class ListRegistrationStudentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Registration
        fields = [ 'course', 'period']