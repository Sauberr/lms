from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
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

    # formatted_students = format_records(students)
    # response = form + formatted_students

    # return HttpResponse(form_html)

    return render(request, 'students/students_list.html', context={'students': students})


@csrf_exempt
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        # student = Student(**request.POST.dict())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:students_list'))
    else:
        form = StudentForm()
    # form_html = f"""
    # <form method="POST">
    #     {form.as_p()}
    #     <button type="submit">Submit</button>
    # </form>
    # """
    # return HttpResponse(form_html)

    return render(request, 'students/students_create.html', context={'form': form})


@csrf_exempt
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
    # form_html = f"""
    # <form method="POST">
    #     {form.as_p()}
    #     <button type="submit">Submit</button>
    # </form>
    # """

    # return HttpResponse(form_html)

    return render(request, 'students/students_edit.html', context={'form': form})


@csrf_exempt
def delete_student(request, pk: int):
    student = get_object_or_404(Student.objects.all(), pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        student.delete()
        return HttpResponseRedirect(reverse('groups:groups_lists'))
    else:
        form = StudentForm(instance=student)
    form_html = f"""
       <form method="POST">
           {form.as_p()}
           <button type="submit">Submit</button>
       </form>
       """

    return HttpResponse(form_html)
