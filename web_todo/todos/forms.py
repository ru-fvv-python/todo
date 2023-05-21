from django import forms


class CategoriesForm(forms.Form):
    """Класс для формы, с помощью которой можно добавлять и редактировать
     категории"""
    name = forms.CharField(label='Название категории')
