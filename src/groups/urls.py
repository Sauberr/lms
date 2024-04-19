from django.urls import path
from groups.views import get_groups, create_group

urlpatterns = [
    path('', get_groups, name='groups_list'),
    path('create/', create_group, name='create_group'),
]
