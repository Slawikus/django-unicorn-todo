from django import forms

from todos.models import Todo


class TodoCreateForm(forms.ModelForm):
    description = forms.CharField(max_length=10, required=True)
    due_date = forms.DateField(required=False)

    class Meta:
        model = Todo
        fields = ('description', 'due_date')

