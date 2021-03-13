from django_unicorn.components import UnicornView


class TodoView(UnicornView):
    todo = None
    is_editing = False

    def delete(self):
        self.todo.delete()
        self.parent.load_todos()

    def toggle_edit(self):
        self.is_editing = not self.is_editing

        if self.is_editing:
            self.call("setFocus")

    def save(self):
        self.todo.save()
        self.is_editing = False
