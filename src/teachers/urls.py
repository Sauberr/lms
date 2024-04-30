from django.urls import path

from teachers.views import (CreateTeacherView, DeleteTeacherView, TeacherListView,
                            UpdateTeacherView, GetTeacherGroupInfoView)

app_name = "teachers"

urlpatterns = [
    path("", TeacherListView.as_view(), name="teachers_list"),
    path("create/", CreateTeacherView.as_view(), name="create_teacher"),
    path("update/<str:pk>/", UpdateTeacherView.as_view(), name="update_teacher"),
    path("delete/<str:pk>/", DeleteTeacherView.as_view(), name="delete_teacher"),
    path("groups/<str:pk>/", GetTeacherGroupInfoView.as_view(), name="teacher_groups")
]
