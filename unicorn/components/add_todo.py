from django_unicorn.components import UnicornView

from todos.models import Todo


class AddTodoView(UnicornView):
    description = None

    def add(self):
        todo = Todo.objects.create(description=self.description)

        self.parent.load_todos()
        self._reset_state()

        return todo

    def _reset_state(self):
        self.description = None
