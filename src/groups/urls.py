from django.urls import path

from groups.views import create_group, delete_group, get_groups, update_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='groups_list'),
    path('create/', create_group, name='create_group'),
    path('update/<str:pk>/', update_group, name='update_group'),
    path('delete/<str:pk>/', delete_group, name='delete_group'),
]
