from django.core.exceptions import ValidationError


def first_name_validator(first_name: str) -> None:
    if 'vova' in first_name.lower():
        raise ValidationError('Vova is not correct name, should be volodimir')


def gpa_validator(gpa, min_value=1, max_value=5) -> float:
    if gpa < min_value:
        raise ValidationError('The minimum value of GPA is 1')
    elif gpa > max_value:
        raise ValidationError('The maximum value of GPA is 5')

    return round(float(gpa), 2)


def median_age_validator(median_age, min_value=0) -> float:
    if median_age < min_value:
        raise ValidationError('The minimum value of median age is 1')

    return round(float(median_age), 2)

