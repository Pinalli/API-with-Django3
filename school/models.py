from django.db import models

class Student(models.Model):
    name = models.CharField(blank=False,max_length=255)
    cpf = models.CharField(blank=False,max_length=11)
    birthday = models.DateField()
    email = models.EmailField(max_length=255,null=True, blank=True) #new field
    active = models.BooleanField(null=True, blank=True) #new field , add null=True, blank=True for existing data
      
    def __str__(self):
        return self.name
    
class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
       ( 'I', 'Intermediate'),
        ('A', 'Advanced')
    )
    code_course = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices = LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.description
    
class Registration(models.Model):
    PERIOD = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False, default='M')

    # def __str__(self):
    #     return self.student.name + ' - ' + self.course.description + ' - ' + self.period