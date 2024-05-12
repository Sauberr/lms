from django import forms
from django.core.exceptions import ValidationError

from teachers.models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    @staticmethod
    def normalize_text(text: str) -> str:
        return text.strip().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        if not first_name.isalpha():
            raise ValidationError('First name mustn\'t contain digits!')

        return self.normalize_text(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        if not last_name.isalpha():
            raise ValidationError('Last name mustn\'t contain digits!')

        return self.normalize_text(last_name)

    def clean_email(self):
        email = self.cleaned_data['email']

        if "@yandex" in email.lower():
            raise ValidationError('Yandex domain is forbidden in our country!')

        return email

    def clean(self):
        cleand_data = super().clean()

        first_name = cleand_data['first_name']
        last_name = cleand_data['last_name']

        if last_name == first_name:
            raise ValidationError('First name and last name can\'t be equal!')

        return cleand_data
