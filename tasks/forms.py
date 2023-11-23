from datetime import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from tasks.models import Task


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def clean_deadline(self):
        if self.cleaned_data["deadline"] < datetime.now().date():
            raise ValidationError("Deadline can not be assigned earlier than today")
        return self.cleaned_data["deadline"]

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "is_completed",
            "priority",
            "task_type",
            "assignees"
        )
