from django.urls import path

from students.views import (CreateStudentView, DeleteView, StudentsListView,
                            UpdateStudentView)

app_name = 'students'

urlpatterns = [
    path('', StudentsListView.as_view(), name='students_list'),
    path('create/', CreateStudentView.as_view(), name='create_student'),
    path('update/<uuid:uuid>/', UpdateStudentView.as_view(), name='update_student'),
    path('delete/<uuid:uuid>/', DeleteView.as_view(), name='delete_student'),
]
