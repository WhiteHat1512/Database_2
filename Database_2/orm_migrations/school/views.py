from django.shortcuts import render
from django.views.generic import ListView

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    student = Student.objects.all().order_by(ordering)
    context = {'object_list': student}

    return render(request, template, context)

