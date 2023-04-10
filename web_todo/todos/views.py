from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

from .models import Task


def index(request):
    """Генерация количеств типов задач"""
    # всего задач
    num_tasks = Task.objects.all().count()

    # количество завершенных задач
    num_tasks_completeness = Task.objects.filter(completeness=1).count()

    # количество не завершенных задач
    num_tasks_opened = Task.objects.filter(completeness=0).count()

    return render(request, 'index.html',
                  context={'num_tasks': num_tasks,
                           'num_tasks_completeness': num_tasks_completeness,
                           'num_tasks_opened': num_tasks_opened},
                  )
