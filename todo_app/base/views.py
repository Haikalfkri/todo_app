from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from base.models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "base/task_list.html"
    context_object_name = "tasks"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "base/task_detail.html"
    context_object_name = "task"
    
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = "base/task_create.html"
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)
    

class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = "base/task_update.html"
    success_url = reverse_lazy('tasks')
    

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "base/task_confirm_delete.html"
    success_url = reverse_lazy("tasks")
    context_object_name = "task"