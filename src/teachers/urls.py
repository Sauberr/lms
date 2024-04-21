from django.urls import path
from teachers.views import get_teachers, create_teacher, update_teacher, delete_teacher

app_name = "teachers"

urlpatterns = [
    path("", get_teachers, name="teachers_list"),
    path("create/", create_teacher, name="create_teacher"),
    path("update/<str:pk>/", update_teacher, name="update_teacher"),
    path("delete/<str:pk>/", delete_teacher, name="delete_teacher"),
]
