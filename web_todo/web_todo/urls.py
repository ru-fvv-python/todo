"""web_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from todos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories-add/', views.categories_add, name='categories-add'),
    path('create-category/', views.create_category, name='create-category'),
    path('delete-category/<int:id>/', views.delete_category,
         name='delete-category'),
    path('edit-category/<int:id>/', views.edit_category, name='edit-category'),
    path('admin/', admin.site.urls),
    re_path(r'^tasks/$', views.TaskListView.as_view(), name='tasks'),
    re_path(r'^task/(?P<pk>\d+)$', views.TaskDetailView.as_view(),
            name='task-detail'),

]

# Добавление URL-адреса для входа в систему
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# Добавление URL-адресов для создания, изменения и удаления задач
urlpatterns += [
    re_path(r'^task/create$', views.TaskCreate.as_view(),
            name='task_create'),
    re_path(r'^task/update/(?P<pk>\d+)$', views.TaskUpdate.as_view(),
            name='task_update'),
    re_path(r'^task/delete/(?P<pk>\d+)$', views.TaskDelete.as_view(),
            name='task_delete'),

]


# Добавление URL-адреса для фильтра задач по владельцу
urlpatterns += [
    re_path(r'^mytasks/$', views.TasksByUserListView.as_view(),
            name='my-tasks',)
]