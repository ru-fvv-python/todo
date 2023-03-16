from django.db import models


# Create your models here.


class Importance(models.Model):
    """Степень важности задачи"""
    name = models.CharField(max_length=20,
                            help_text='Введите важность задачи',
                            verbose_name='Степень важности')

    def __str__(self):
        """возвращает важность задачи"""
        return self.name


class Category(models.Model):
    """Категория"""
    name = models.CharField(max_length=50,
                            help_text='Введите категорию',
                            verbose_name='Категория')

    def __str__(self):
        """Возвращает категорию"""
        return self.name


class Task(models.Model):
    """Задача"""
    name = models.CharField(max_length=100,
                            help_text='Введите название задачи',
                            verbose_name='Задача')
    date_from = models.DateField(help_text='Введите дату начала задачи',
                                 verbose_name='Дата начала')
    date_to = models.DateField(help_text='Введите дату завершения задачи',
                               verbose_name='Дата завершения')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 help_text='Выберите категорию',
                                 verbose_name='Категория')
    importance = models.ForeignKey('Importance', on_delete=models.CASCADE,
                                   help_text='выберите важность задачи',
                                   verbose_name='Важность')
    completeness = models.BooleanField(default=False,
                                       help_text='Задача завершена?',
                                       verbose_name='Статус выполнения')

    def __str__(self):
        """Возваращает задачу"""
        return '%s %s' % (self.name, self.completeness)
