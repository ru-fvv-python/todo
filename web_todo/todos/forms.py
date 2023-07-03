from django import forms
from django.forms import ModelForm

from .models import Task


class CategoriesForm(forms.Form):
    """Класс для формы, с помощью которой можно добавлять и редактировать
     категории"""
    name = forms.CharField(label='Название категории')


class TaskModelForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'date_from', 'date_to', 'category', 'importance',
                  'completeness', 'owner']