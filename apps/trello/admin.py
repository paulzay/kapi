from django.contrib import admin
from apps.trello.models import Column, Task

admin.site.register(Column)
admin.site.register(Task)
# Register your models here.
