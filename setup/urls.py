
from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, RegistrationViewSet,  ListRegistrationsStudent, ListStudentsRegistration
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('registrations', RegistrationViewSet, basename='Registrations')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/registrations/',  ListRegistrationsStudent.as_view()),
    path('courses/<int:pk>/registrations/',   ListStudentsRegistration.as_view()),
]
