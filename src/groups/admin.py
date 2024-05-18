from django.contrib import admin

from groups.models import Group


@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    list_display = ('title', )
