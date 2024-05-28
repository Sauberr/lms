from django.contrib import admin
from django import forms

from groups.models import Group
from students.models import Student
from teachers.models import Teacher


class TeacherAdminInline(admin.StackedInline):
    model = Teacher.groups.through
    extra = 0


class StudentAdminInline(admin.StackedInline):
    model = Student
    extra = 0


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    comments = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    send_email = forms.BooleanField()

    def clean_max_count_of_students(self):
        if self.cleaned_data['max_count_of_students'] < 1:
            raise forms.ValidationError('Max count of students must be greater than 0!')
        if self.cleaned_data['max_count_of_students'] > 100:
            raise forms.ValidationError('Max count of students must be less than 100!')
        return self.cleaned_data['max_count_of_students']

    def save(self, commit=True):
        print([self.cleaned_data['comments']])
        print(self.cleaned_data['email'])
        if self.cleaned_data['send_email'] and self.cleaned_data['email']:
            print('Email sent!')

        return super().save(commit=commit)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [StudentAdminInline, TeacherAdminInline]
    form = GroupForm
    actions = ['count_to_zero']

    @admin.action(description='Set to zero of count of selected groups')
    def count_to_zero(self, request, queryset):
        queryset.update(max_count_of_students=0)


