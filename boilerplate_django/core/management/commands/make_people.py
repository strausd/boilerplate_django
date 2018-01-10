from django.core.management.base import BaseCommand

from boilerplate_django.core.models.base import Person


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Person.objects.all().count() == 0:
            Person.objects.create(name='Preston Horn')
            Person.objects.create(name='Willie Wrinkle')
            Person.objects.create(name='Danny Straus')
