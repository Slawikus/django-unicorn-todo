from django_unicorn.components import UnicornView

from todos.models import Todo


class TodoListView(UnicornView):
    todos = Todo.objects.none()

    def hydrate(self):
        self.load_todos()

    def delete(self, id):
        self.todos.get(pk=id).delete()

    def load_todos(self):
        self.todos = Todo.objects.all()
