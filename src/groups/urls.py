from django.urls import path
from groups.views import get_groups, create_group, update_group, delete_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='groups_list'),
    path('create/', create_group, name='create_group'),
    path('update/<str:pk>/', update_group, name='update_group'),
    path('delete/<str:pk>/', delete_group, name='delete_group'),
]
