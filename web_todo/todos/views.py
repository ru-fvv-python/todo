# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import CategoriesForm
from .models import Task, Category


class TaskCreate(CreateView):
    """Класс для создания Задачи"""
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    """Класс для изменения Задачи"""
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    """Класс для удаления Задачи"""
    model = Task
    success_url = reverse_lazy('tasks')


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
    """Универсальный класс представления списка задач
    конкретного пользователя"""

    model = Task
    template_name = 'todos/task_list_owner_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('date_to')


def categories_add(request):
    """получение данных из БД и загрузка шаблона categories_add.html"""

    category = Category.objects.all()
    categories_form = CategoriesForm()
    return render(request, 'todos/categories_add.html',
                  {'form': categories_form, 'category': category})


def create_category(request):
    """сохранение категорий в бд"""
    if request.method == 'POST':
        category = Category()
        category.name = request.POST.get('name')
        category.save()
        return HttpResponseRedirect('/categories-add/')


def delete_category(request, id):
    """удаление категории из бд"""
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return HttpResponseRedirect('/categories-add/')
    except Category.DoesNotExist:
        return HttpResponseNotFound('<h2>Категория не найдена</h2>')


def edit_category(request, id):
    """редактирование категории в БД"""
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category.name = request.POST.get('name')
        category.save()
        return HttpResponseRedirect('/categories-add/')
    else:
        return render(request, 'todos/category_edit.html',
                      {'category': category})
