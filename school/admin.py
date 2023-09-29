from django.contrib import admin
from school.models import Student, Course, Registration

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'birthday')
    list_display_links = ('id', 'name') # links to edit
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'code_course', 'description')
    list_display_links = ('id', 'code_course')
    search_fields = ('code_course',)
    list_per_page = 20

admin.site.register(Course, Courses)

class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id', )  

admin.site.register(Registration, Registrations)