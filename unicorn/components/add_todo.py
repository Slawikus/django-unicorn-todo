from django_unicorn.components import UnicornView

from todos.models import Todo


class AddTodoView(UnicornView):
    description = ''
    due_date = None

    def add(self):
        todo = Todo.objects.create(description=self.description, due_date=self.due_date)

        self.parent.load_todos()
        self.description = ''
        self.due_date = None

        return todo
