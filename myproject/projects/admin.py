from django.contrib import admin
from .models import Client
from .models import Project
from .models import Task

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Task)