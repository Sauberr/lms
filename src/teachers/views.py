from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

from teachers.forms import TeacherForm
from teachers.models import Teacher


class TeacherListView(ListView):
    template_name = "teachers/teachers_list.html"
    model = Teacher
    context_object_name = 'teachers'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Teacher.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        else:
            return Teacher.objects.all()


class CreateTeacherView(CreateView):
    template_name = "teachers/teachers_create.html"
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('teachers:teachers_list')


class UpdateTeacherView(UpdateView):
    template_name = "teachers/teachers_edit.html"
    model = Teacher
    form_class = TeacherForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('teachers:teachers_list')
    queryset = Teacher.objects.all()


class DeleteTeacherView(DeleteView):
    template_name = "teachers/teachers_delete.html"
    model = Teacher
    success_url = reverse_lazy('teachers:teachers_list')
    pk_url_kwarg = 'pk'
    queryset = Teacher.objects.all()


class GetTeacherGroupInfoView(DetailView):
    template_name = "teachers/teacher_groups.html"
    model = Teacher
    pk_url_kwarg = "pk"
    context_object_name = "teacher"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = self.object.groups.all()
        return context

