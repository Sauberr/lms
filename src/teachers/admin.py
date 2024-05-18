from django.contrib import admin
from django.utils.html import format_html

from teachers.models import Teacher

from django.urls import reverse


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group_count', 'links_to_groups')
    # fields = ('first_name', 'last_name', 'salary', 'groups')
    fieldsets = (
        (
          "Personal info",
          {"fields": ('first_name', 'last_name')}
        ),
        (
            "Salary info",
            {"fields": ('salary',)}
        ),
        (
            "Groups",
            {"classes": ('collapse',),
             "fields": ('groups',)}
        ),
        (
            "Additional info",
            {"fields": ('age', 'experience', 'sex')}
        )
    )

    def group_count(self, obj) -> int:
        if obj.groups:
            return obj.groups.count()
        return 0

    def links_to_groups(self, obj) -> str:
        if obj.groups:
            groups = obj.groups.all()
            links = []
            for group in groups:
                links.append(
                    f"<a class='button' href='{reverse('admin:groups_group_change', args=[group.pk])}'>{group.title}</a>"
                )
            return format_html("<br>".join(links))
        return "No groups found"
