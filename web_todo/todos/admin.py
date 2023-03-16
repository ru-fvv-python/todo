from django.contrib import admin
from .models import Category, Importance, Task
# Register your models here.

admin.site.register(Category)
admin.site.register(Importance)
admin.site.register(Task)

