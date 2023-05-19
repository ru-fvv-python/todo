# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .models import Task


class TaskListView(generic.ListView):
    """Обобщенный класс для вывода списка задач"""
    model = Task
    paginate_by = 3


class TaskDetailView(generic.DetailView):
    """Класс для вывода определенной задачи"""
    model = Task


def index(request):
    """Генерация количеств типов задач"""
    # всего задач
    num_tasks = Task.objects.all().count()

    # количество завершенных задач
    num_tasks_completeness = Task.objects.filter(completeness=1).count()

    # количество не завершенных задач
    num_tasks_opened = Task.objects.filter(completeness=0).count()

    # количество посещений этого представления, посчитанное в переменной session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html',
                  context={'num_tasks': num_tasks,
                           'num_tasks_completeness': num_tasks_completeness,
                           'num_tasks_opened': num_tasks_opened,
                           'num_visits': num_visits},
                  )


class TasksByUserListView(LoginRequiredMixin, generic.ListView):
    """Универсальный класс представления списка задач конкретного пользователя"""

    model = Task
    template_name = 'todos/task_list_owner_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('date_to')
