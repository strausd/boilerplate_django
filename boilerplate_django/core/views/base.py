from django.shortcuts import render

from boilerplate_django.core.models.base import Person


def homepage(request):
    return render(request, 'base.html', { 'people': Person.objects.all() })
