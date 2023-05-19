from django.contrib import admin

from .models import Task, Category, Importance


# Register your models here.

# admin.site.register(Category)
# admin.site.register(Importance)
# admin.site.register(Task)

class TaskAdmin(admin.ModelAdmin):
    """определение к классу задач"""
    # очередность полей в списке
    list_display = (
        'category', 'importance', 'completeness', 'name', 'date_from',
        'date_to', 'owner')
    # фильтры
    list_filter = ('category', 'importance', 'completeness', 'owner')
    # секции с полями
    fieldsets = (
        ('Задача', {
            'fields': ('name', 'category', 'importance')
        }),
        ('Статус и сроки', {
            'fields': ('completeness', ('date_from', 'date_to'), 'owner')
        })
    )


# регистрация класса TaskAdmin с моделью Task
admin.site.register(Task, TaskAdmin)


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """определение к классу категорий
    регистрация класса CategoryAdmin с моделью Category"""
    list_display = ('name',)
    inlines = [TaskInline]


@admin.register(Importance)
class ImportanceAdmin(admin.ModelAdmin):
    """определение к классу важности задачи
        регистрация класса ImportanceAdmin с моделью Importance"""
    list_display = ('name',)
