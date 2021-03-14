from django_unicorn.components import UnicornView


class TodoView(UnicornView):
    todo = None

    def delete(self):
        self.todo.delete()
        self.parent.load_todos()
