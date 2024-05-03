from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from webargs import fields
from webargs.djangoparser import use_kwargs

from students.forms import StudentForm
from students.models import Student
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView


class IndexView(TemplateView):
    template_name = "partials/index.html"
    extra_context = {'title': 'Home'}
    http_method_names = ['get']


class StudentsListView(LoginRequiredMixin, ListView):
    template_name = "students/students_list.html"
    model = Student
    context_object_name = 'students'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        else:
            return Student.objects.all()


class CreateStudentView(LoginRequiredMixin, CreateView):
    template_name = "students/students_create.html"
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:students_list')


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    template_name = "students/students_edit.html"
    model = Student
    form_class = StudentForm
    pk_url_kwarg = 'uuid'
    success_url = reverse_lazy('students:students_list')
    queryset = Student.objects.all()


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    template_name = "students/students_delete.html"
    model = Student
    success_url = reverse_lazy('students:students_list')
    pk_url_kwarg = 'uuid'
    queryset = Student.objects.all()
