from django.urls import path

from students.views import (create_student, delete_student, get_students,
                            update_student)

app_name = 'students'

urlpatterns = [
    path('', get_students, name='students_list'),
    path('create/', create_student, name='create_student'),
    path('update/<uuid:uuid>/', update_student, name='update_student'),
    path('delete/<uuid:uuid>/', delete_student, name='delete_student'),
]
