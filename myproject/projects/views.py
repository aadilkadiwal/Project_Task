from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import User
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

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'

    # Only that project will show whoes end date and time is greter then current date and time 
    queryset = Project.objects.filter(Q(end_date__gte=timezone.now())) 

    # The close end_date will show on top
    ordering = ['end_date']

    # In 1 page 2 project should be there
    paginate_by = 5

# To display only that project which user has created
class UserProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/user_projects.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'

    # Only that project will show whoes end date and time is greter then current date and time 
    # queryset = Project.objects.filter(Q(end_date__gte=timezone.now())) 

    # In 1 page 2 project should be there
    paginate_by = 5   

    # To check user by username
    def get_queryset(self):

        # If user exist then we will capture them in user variable and if user doesn't exist then it will return 404 
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(created_by=user).order_by('-end_date')

class ProjectDetailView(LoginRequiredMixin, DetailView):
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

        # To check correct user is deleting project or not
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