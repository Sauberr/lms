from groups.models import Group
from students.utils.helpers import format_records
from webargs import fields
from django.db.models import Q
from webargs.djangoparser import use_kwargs
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@use_kwargs(
    {
        "title": fields.Str(required=False),
        "department": fields.Str(required=False),
        "search_text": fields.Str(required=False),
    },
    location="query",
)
def get_groups(request, **kwargs):
    form = """
    <form>
        <label for="title">Title:</label><br>
        <input type="title" id="title" name="title"><br>

        <label for="department">Department:</label><br>
        <input type="text" id="department" name="department"><br>

        <label for="search_text">Search:</label><br>
        <input type="text" id="search_text" name="search_text"><br><br>

        <button type="submit">Submit</button>
    </form>
    """

    groups = Group.objects.all()

    search_fields = ["title", "department"]

    for field_name, field_value in kwargs.items():

        if field_name == "search_text":
            or_filter = Q()
            for field in search_fields:
                # accumulate filter condition
                or_filter |= Q(**{f"{field}__icontains": field_value})
            groups = groups.filter(or_filter)
        else:
            if field_value:
                groups = groups.filter(**{field_name: field_value})

    formatted_teachers = format_records(groups)
    response = form + formatted_teachers

    return HttpResponse(response)


@csrf_exempt
def create_group(request):
    form = """

            <form method="POST">
                <label for="Title">Title:</label><br>
                <input type="text" id="title" name="title"><br>

                <label for="department">Department:</label><br>
                <input type="text" id="department" name="department"><br>

                <button type="submit">Submit</button>
            </form>

            """

    if request.method == "POST":
        group = Group(**request.POST.dict())
        group.save()
        return HttpResponseRedirect("/groups")
    elif request.method == "GET":
        ...
    return HttpResponse(form)
