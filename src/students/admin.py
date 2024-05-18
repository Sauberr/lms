from django.contrib import admin

from students.models import Student, Group


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'group', 'gpa', 'grade')
    list_filter = ('group', 'grade')
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






