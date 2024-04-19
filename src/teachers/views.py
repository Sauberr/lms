from teachers.models import Teacher
from students.utils.helpers import format_records
from webargs import fields
from django.db.models import Q
from webargs.djangoparser import use_kwargs
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@use_kwargs(
    {
        "first_name": fields.Str(required=False),
        "last_name": fields.Str(required=False),
        "sex": fields.Str(required=False),
        "search_text": fields.Str(required=False),
    },
    location="query",
)
def get_teachers(request, **kwargs):
    form = """
    <form>
        <label for="first_name">First Name:</label><br>
        <input type="text" id="first_name" name="first_name"><br>
    
        <label for="last_name">Last Name:</label><br>
        <input type="text" id="last_name" name="last_name"><br>
    
        <label for="sex">Sex:</label><br>
        <input type="text" id="sex" name="sex"><br>
    
        <label for="search_text">Search:</label><br>
        <input type="text" id="search_text" name="search_text"><br><br>

        <button type="submit">Submit</button>
    </form>
    """

    teachers = Teacher.objects.all()

    search_fields = ["last_name", "first_name", "sex"]

    for field_name, field_value in kwargs.items():

        if field_name == "search_text":
            or_filter = Q()
            for field in search_fields:
                # accumulate filter condition
                or_filter |= Q(**{f"{field}__icontains": field_value})
            teachers = teachers.filter(or_filter)
        else:
            if field_value:
                teachers = teachers.filter(**{field_name: field_value})

    formatted_teachers = format_records(teachers)
    response = form + formatted_teachers

    return HttpResponse(response)


@csrf_exempt
def create_teacher(request):
    form = """

            <form method="POST">
                <label for="first_name">First Name:</label><br>
                <input type="text" id="first_name" name="first_name"><br>

                <label for="last_name">Last Name:</label><br>
                <input type="text" id="last_name" name="last_name"><br>

                <label for="sex">Sex:</label><br>
                <input type="sex" id="sex" name="sex"><br><br>

                <button type="submit">Submit</button>
            </form>

            """

    if request.method == "POST":
        teacher = Teacher(**request.POST.dict())
        teacher.save()
        return HttpResponseRedirect("/teachers")
    elif request.method == "GET":
        ...
    return HttpResponse(form)
