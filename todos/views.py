from django.views.generic import ListView

from todos.models import Todo


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'
