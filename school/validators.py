from rest_framework import serializers
from school.models import Course, Student, Registration

def validate_cpf(cpf):
    if len(cpf) != 11:
            raise serializers.ValidationError("The CPF need to have 11 digits")
    if(not cpf.isnumeric()):
            raise serializers.ValidationError("The CPF need to have only numbers")
    if(Student.objects.filter(cpf=cpf).exists()):
            raise serializers.ValidationError("This CPF already exists")
    return cpf

def validate_name(name):
    if len(name) < 5:
            raise serializers.ValidationError("The name need to have more than 5 characters")
#     elif(name.isnumeric()):
#             raise serializers.ValidationError("The name need to have only letters")
#     elif(Student.objects.filter(name=name).exists()):
#             raise serializers.ValidationError("This name already exists")
    return name

def validate_birthday(birthday):
    if(birthday.year < 1900):
           raise serializers.ValidationError("The year of birthday need to be greater than 1900")
    if(birthday.year > 2005):
           raise serializers.ValidationError("The year of birthday need to be less than 2005, the student need to be older than 16 years old")
    return birthday

def validate_email( email):
    if(Student.objects.filter(email=email).exists()):
            raise serializers.ValidationError("This email already exists")
    if(email.find('@') == -1):
            raise serializers.ValidationError("The email need to have @")
    if(email.find('.') == -1):
            raise serializers.ValidationError("The email need to have .")
    return email