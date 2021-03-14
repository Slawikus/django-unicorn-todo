from django_unicorn.components import UnicornView

from todos.models import Todo


class AddTodoView(UnicornView):
    description = None

    def add(self):
        Todo.objects.create(description=self.description)
        self.description = None
        self.parent.load_todos()
