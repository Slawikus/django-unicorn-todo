from django_unicorn.components import UnicornView

from todos.models import Todo


class TodoListView(UnicornView):
    todos = Todo.objects.none()
    description = None

    def hydrate(self):
        self.load_todos()

    def delete(self, id):
        Todo.objects.get(pk=id).delete()

    def load_todos(self):
        self.todos = Todo.objects.all()

    def add(self):
        todo = Todo.objects.create(description=self.description)

        self.load_todos()
        self.description = None

        return todo
