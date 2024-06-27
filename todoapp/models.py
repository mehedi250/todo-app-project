from django.db import models
from django.contrib.auth.models import User

class todo(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        IN_PROGRESS = 'In progress', 'In progress'
        COMPLETED = 'Completed', 'Completed'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=1000)
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.PENDING
    )

    def __str__(self):
        return self.todo_name