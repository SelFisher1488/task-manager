from django.contrib.auth.models import AbstractUser
from django.db import models

from task_manager.settings import AUTH_USER_MODEL


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        ordering = ["username"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} (position{self.position})"


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("urgent", "Urgent"),
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
        ("optional", "Optional")
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField()
    priority = models.CharField(
        max_length=255,
        choices=PRIORITY_CHOICES,
        default="low"
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="tasks"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} better to do by:{self.deadline}"

