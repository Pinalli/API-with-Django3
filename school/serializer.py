from rest_framework import serializers
from school.models import Course, Student, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'cpf', 'birthday']
    def validate_cpf(self, cpf):
            if len(cpf) != 11:
                raise serializers.ValidationError("The CPF need to have 11 digits")
            if(not cpf.isnumeric()):
                raise serializers.ValidationError("The CPF need to have only numbers")
            if(Student.objects.filter(cpf=cpf).exists()):
                raise serializers.ValidationError("This CPF already exists")
            return cpf
    def validate_name(self, name):
            if len(name) < 5:
                raise serializers.ValidationError("The name need to have more than 5 characters")
            if(name.isnumeric()):
                raise serializers.ValidationError("The name need to have only letters")
            if(Student.objects.filter(name=name).exists()):
                raise serializers.ValidationError("This name already exists")
            return name
    def validate_birthday(self, birthday):
        if(birthday.year < 1900):
            raise serializers.ValidationError("The year of birthday need to be greater than 1900")
        if(birthday.year > 2005):
            raise serializers.ValidationError("The year of birthday need to be less than 2005, the student need to be older than 16 years old")
        return birthday
      

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