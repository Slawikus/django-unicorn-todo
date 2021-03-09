from django.db import models


class Todo(models.Model):
    description = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField()
