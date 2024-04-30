from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from groups.forms import GroupForm
from groups.models import Group


class GroupListView(ListView):
    model = Group
    template_name = 'groups/groups_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Group.objects.filter(Q(title__icontains=query) | Q(department__icontains=query))
        else:
            return Group.objects.all()


class CreateGroupView(CreateView):
    template_name = "groups/groups_create.html"
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy('groups:groups_list')


class UpdateGroupView(UpdateView):
    template_name = "groups/groups_edit.html"
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy('groups:groups_list')
    pk_url_kwarg = 'pk'
    queryset = Group.objects.all()


class DeleteGroupView(DeleteView):
    template_name = "groups/groups_delete.html"
    model = Group
    success_url = reverse_lazy('groups:groups_list')
    pk_url_kwarg = 'pk'
    queryset = Group.objects.all()
