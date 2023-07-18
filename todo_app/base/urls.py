from django.urls import path
from base import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="tasks"),
    path("task_detail/<int:pk>/", views.TaskDetailView.as_view(), name="task"),
    path("task_create", views.TaskCreateView.as_view(), name="create_task"),
    path("edit_task/<int:pk>/", views.UpdateTaskView.as_view(), name="update_task"),
    path("delete_task/<int:pk>/", views.DeleteTaskView.as_view(), name="task_delete")
]
