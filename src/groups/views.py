from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from webargs import fields
from webargs.djangoparser import use_kwargs

from groups.forms import GroupForm
from groups.models import Group
from students.utils.helpers import format_records


@use_kwargs(
    {
        "title": fields.Str(required=False),
        "department": fields.Str(required=False),
        "search_text": fields.Str(required=False),
    },
    location="query",
)
def get_groups(request, **kwargs):
    # form = """
    # <form>
    #     <label for="title">Title:</label><br>
    #     <input type="title" id="title" name="title"><br>
    #
    #     <label for="department">Department:</label><br>
    #     <input type="text" id="department" name="department"><br>
    #
    #     <label for="search_text">Search:</label><br>
    #     <input type="text" id="search_text" name="search_text"><br><br>
    #
    #     <button type="submit">Submit</button>
    # </form>
    # """

    query = request.GET.get('q')

    if query:
        groups = Group.objects.filter(
            Q(title__icontains=query) | Q(department__icontains=query))
    else:
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

    # formatted_teachers = format_records(groups)
    # response = form + formatted_teachers
    #
    # return HttpResponse(response)

    return render(request, 'groups/groups_list.html', context={'groups': groups})


def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("group:groups_list"))
    else:
        form = GroupForm()
    # form_html = f"""
    #         <form method="POST">
    #             {form.as_p()}
    #             <button type="submit">Submit</button>
    #         </form>
    #         """
    # return HttpResponse(form_html)

    return render(request, 'groups/groups_create.html', context={'form': form})


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("groups:groups_list"))
    else:
        form = GroupForm(instance=group)
    # form_html = f"""
    #         <form method="POST">
    #             {form.as_p()}
    #             <button type="submit">Submit</button>
    #         </form>
    #         """
    # return HttpResponse(form_html)

    return render(request, 'groups/groups_edit.html', context={'form': form})


def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        group.delete()
        return HttpResponseRedirect(reverse('groups:groups_list'))
    else:
        form = GroupForm(instance=group)
    # form_html = f"""
    #    <form method="POST">
    #        {form.as_p()}
    #        <button type="submit">Submit</button>
    #    </form>
    #    """
    #
    # return HttpResponse(form_html)

    return render(request, 'groups/groups_delete.html', context={'form': form})
