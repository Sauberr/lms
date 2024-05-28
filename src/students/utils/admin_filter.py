from django.contrib import admin
from datetime import date


class AgeRangeListFilter(admin.SimpleListFilter):
    title = 'Age range filter'

    parameter_name = 'age_range'

    def lookups(self, request, model_admin):
        return (
            (1, '5-21'),
            (2, '22-40'),
            (3, '41-60'),
            (4, '61-80'),
            (5, '81-100'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(birth_date__gte=date(2001, 1, 1),
                                   birth_date__lte=date(2019, 12, 31))
        if self.value() == '2':
            return queryset.filter(birth_date__gte=date(1980, 1, 1),
                                   birth_date__lte=date(2000, 12, 31))
        if self.value() == '3':
            return queryset.filter(birth_date__gte=date(1960, 1, 1),
                                   birth_date__lte=date(1980, 12, 31))
        if self.value() == '4':
            return queryset.filter(birth_date__gte=date(1940, 1, 1),
                                   birth_date__lte=date(1960, 12, 31))
        if self.value() == '5':
            return queryset.filter(birth_date__gte=date(1920, 1, 1),
                                   birth_date__lte=date(1940, 12, 31))