from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import TextChoices
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='projects', on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField()  

    def __str__(self):
        return self.name  

class Task(models.Model):
    class Status(TextChoices):
        todo = 'TO DO'
        wip = 'WIP'
        onhold = 'ONHOLD'
        done = 'DONE'
    name = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=Status.choices, default=Status.todo)

    def __str__(self):
        return self.name