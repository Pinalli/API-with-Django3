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

class ListRegistrationsStudentSerializer(serializers.ModelSerializer):

    course = serializers.ReadOnlyField(source='course.description')  
    period = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = [ 'course', 'period']
    def get_period(self, obj):
        return obj.get_period_display()
    
class ListStudentsRegistrationSerializer(serializers.ModelSerializer):   
    student_name = serializers.ReadOnlyField(source='students.name') 
    class Meta:
        model = Registration
        fields = [ 'student_name']