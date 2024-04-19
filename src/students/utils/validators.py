from django.core.exceptions import ValidationError


def first_name_validator(first_name: str) -> None:
    if 'vova' in first_name.lower():
        raise ValidationError('Vova is not correct name, should be volodimir')
