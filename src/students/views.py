from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from webargs import fields
from webargs.djangoparser import use_kwargs

from students.forms import StudentForm
from students.models import Student
from students.utils.helpers import format_records


def index(request):
    return render(request, 'partials/index.html', context={'key': 'value'})


@use_kwargs(
    {
        "first_name": fields.Str(required=False),
        "last_name": fields.Str(required=False),
        "search_text": fields.Str(required=False),
    },
    location="query",
)
def get_students(request, **kwargs):

    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)
        )
    else:
        students = Student.objects.all()

    search_fields = ["last_name", "first_name", "email"]

    for field_name, field_value in kwargs.items():

        if field_name == "search_text":
            or_filter = Q()
            for field in search_fields:
                # accumulate filter condition
                or_filter |= Q(**{f"{field}__icontains": field_value})
            students = students.filter(or_filter)
        else:
            if field_value:
                students = students.filter(**{field_name: field_value})

    return render(request, 'students/students_list.html', context={'students': students})


def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        # student = Student(**request.POST.dict())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:students_list'))
    else:
        form = StudentForm()

    return render(request, 'students/students_create.html', context={'form': form})


def update_student(request, pk: int):
    student = get_object_or_404(Student.objects.all(), pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        # student = Student(**request.POST.dict())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:groups_lists'))
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/students_edit.html', context={'form': form})


def delete_student(request, pk: int):
    student = get_object_or_404(Student.objects.all(), pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        student.delete()
        return HttpResponseRedirect(reverse('students:students_list'))
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/students_delete.html', context={'form': form, 'student': student})
