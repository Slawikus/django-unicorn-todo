from django_unicorn.components import UnicornView

from todos.models import Todo


class TodoListView(UnicornView):
    todos = Todo.objects.none()
    description = None

    def hydrate(self):
        self.load_todos()

    def add(self):
        Todo.objects.create(description=self.description)
        self.description = None

    def delete(self, id):
        self.todos.get(pk=id).delete()

    def load_todos(self):
        self.todos = Todo.objects.all()
