from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from todos.models import Todo


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'


class TodoCreateView(CreateView):
    model = Todo
    fields = ('description', 'due_date',)
    template_name = 'todos/todo_create.html'
    success_url = reverse_lazy('todo_list')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ('description', 'due_date', 'is_completed')
    template_name = 'todos/todo_update.html'
    success_url = reverse_lazy('todo_list')
