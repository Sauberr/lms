from django.urls import path
from teachers.views import get_teachers, create_teacher

urlpatterns = [
    path("", get_teachers, name="teachers_list"),
    path("create/", create_teacher, name="create_teacher"),
]
