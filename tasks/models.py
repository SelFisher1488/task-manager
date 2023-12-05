from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ["username"]

    def __str__(self) -> str:
        return (
            f"{self.first_name} {self.last_name} (position: {self.position})"
        )

    def get_absolute_url(self):
        return reverse("tasks:worker-detail", kwargs={"pk": self.pk})


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("Urgent", "1"),
        ("High", "2"),
        ("Medium", "3"),
        ("Low", "4"),
        ("Optional", "Optional"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=255, choices=PRIORITY_CHOICES, default="4"
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(
        get_user_model(), related_name="tasks", blank=True
    )

    class Meta:
        ordering = ["deadline"]

    def __str__(self) -> str:
        return f"{self.name} better to do by: {self.deadline}"

    def before_deadline(self):
        return self.deadline >= datetime.now().date()
