from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export.fields import Field

from students.models import Student
from students.utils.admin_filter import AgeRangeListFilter


class StudentResource(resources.ModelResource):
    birth_date = Field()

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'birth_date')
        export_order = ('first_name', 'last_name', 'birth_date')

    def dehydrate_birth_date(self, student):
        return student.birth_date.strftime('%Y-%m-%d')


@admin.register(Student)
class StudentAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = StudentResource
    list_display = ('first_name', 'last_name', 'email', 'group', 'gpa', 'grade')
    list_filter = ('group', 'grade', AgeRangeListFilter)
    list_display_links = ('email', )
    date_hierarchy = 'birth_date'
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name', 'group__title')
    fields = ('first_name', 'last_name', 'email', 'group', 'gpa', 'grade', 'birth_date', 'department', 'resume')
    readonly_fields = ('gpa',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('group',)
        return self.readonly_fields

    def links_to_groups(self, obj):
        if obj.groups:
            groups = obj.groups.all()
            links = []
            for group in groups:
                links.append(
                    f"<a class='button' href='{reverse('admin:student_group_change', args=[group.id])}'"
                    f">{group.title}</a>"
                )
                return format_html("</br>".join(links))
        return "No groups found"






