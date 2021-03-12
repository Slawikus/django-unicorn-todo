from todos.models import Todo
from django_unicorn.components import UnicornView


class TodosView(UnicornView):
    todos = Todo.objects.none()

    def hydrate(self):
        self.load_todos()

    def delete(self, id):
        Todo.objects.get(pk=id).delete()

    def load_todos(self):
        self.todos = Todo.objects.all()
