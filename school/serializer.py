from rest_framework import serializers
from school.models import Course, Student, Registration
from school.validators import validate_cpf, validate_name, validate_birthday, validate_email   

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'cpf', 'birthday', 'email', 'active'] 

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"This CPF need to have 11 digits"})           
        if not validate_name(data['name']):
            raise serializers.ValidationError({'name':"The name need to have more than 5 characters"})       
        if not validate_birthday(data['birthday']):
            raise serializers.ValidationError({'birthday':"The year of birthday need to be greater than 1900"})
        if not validate_email(data['email']):
            raise serializers.ValidationError({'email':"The email need to have @ and ."})
        if not data['active']:
            data['active'] = False
        return data
    
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
    student_name = serializers.ReadOnlyField(source='student.name') 
    class Meta:
        model = Registration
        fields = [ 'student_name']