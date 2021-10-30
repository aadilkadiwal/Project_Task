from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Project, Task

def project(request):
    context = {
        'projects' : Project.objects.all()
    }
    return render(request, 'projects/project.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    queryset = Project.objects.filter(Q(end_date__gte=timezone.now())) 
    ordering = ['-start_date']

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/task.html' # <app>/<model>_<viewtype>.html  

# LoginRequiredMixin : can't create a new project without login
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description', 'client', 'start_date', 'end_date']

    def form_valid(self, form):
        # The project is created_by the user who is login
        form.instance.created_by = self.request.user
        messages.success(self.request, f'New Project has been created!')
        return super().form_valid(form)

# LoginRequiredMixin : can't update a new project without login
# UserPassesTestMixin : can't update a project if you not created a project
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'client', 'start_date', 'end_date']

    def form_valid(self, form):

        # The project is created_by the user who is login
        form.instance.created_by = self.request.user
        messages.success(self.request, f'Project has been Updated!')
        return super().form_valid(form)        

    def test_func(self):

        # Updating a current project
        project = self.get_object()

        # To check correct user is updating project or not
        if self.request.user == project.created_by:
            return True
        else:
            return False    

# LoginRequiredMixin : can't delete a project without login
# UserPassesTestMixin : can't delete a project if you not created a project
class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project

    # After deleting a project it will return to home page
    success_url = '/'

    def test_func(self):

        # Updating a current project
        project = self.get_object()

        # To check correct user is updating project or not
        if self.request.user == project.created_by:
            return True
        else:
            return False        

# LoginRequiredMixin : can't create a new task without login
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'project', 'status']

    def form_valid(self, form):

        # The Task is created_by the user who is login
        form.instance.created_by = self.request.user
        messages.success(self.request, f'New Task has been created!')
        return super().form_valid(form)          

# LoginRequiredMixin : can't update task without login
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'project', 'status']

    def get(self, *args, **kwargs):
        pk1 = kwargs.get('pk1', None)
        print(pk1)
        return super(TaskUpdateView, self).get(*args, **kwargs)

    def form_valid(self, form):

        # The task is created_by the user who is login (Error)
        form.instance.created_by = self.request.user
        messages.success(self.request, f'Task has been Updated!')
        return super().form_valid(form)        

# LoginRequiredMixin : can't delete a task without login
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    # After deleting a deleting it will return to home page
    success_url = '/'             