from django.shortcuts import render
from .models import Project

def project(request):
    context = {
        'projects' : Project.objects.all()
    }
    return render(request, 'projects/project.html', context)