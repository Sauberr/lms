from django.urls import path

from groups.views import CreateGroupView, DeleteGroupView, GroupListView, UpdateGroupView

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='groups_list'),
    path('create/', CreateGroupView.as_view(), name='create_group'),
    path('update/<str:pk>/', UpdateGroupView.as_view(), name='update_group'),
    path('delete/<str:pk>/', DeleteGroupView.as_view(), name='delete_group'),
]
