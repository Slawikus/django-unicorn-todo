from django_unicorn.components import UnicornView

from todos.forms import TodoCreateForm
from todos.models import Todo


class AddTodoView(UnicornView):
    form_class = TodoCreateForm

    description = None
    due_date = None

    def add(self):
        if not self.is_valid():
            return self.validate()

        todo = Todo.objects.create(description=self.description, due_date=self.due_date)

        self.parent.load_todos()
        self._reset_state()

        return todo

    def _reset_state(self):
        self.description = None
        self.due_date = None
