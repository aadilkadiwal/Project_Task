from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-home'),
    path('user/<str:username>', views.UserProjectListView.as_view(), name='user-projects'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', views.ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
    path('project/<int:pk>/task/new/', views.TaskCreateView.as_view(), name='task-create'),
    path('project/<int:pk1>/task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('project/<int:pk1>/task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
]
