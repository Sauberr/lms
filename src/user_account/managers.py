from django.db.models import Manager


class PeopleManager(Manager):
    def get_staff_users(self):
        return super().get_queryset().filter(is_staff=True)

