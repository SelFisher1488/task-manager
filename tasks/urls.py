from django.urls import path, include

from tasks.views import (
    home,
    TaskListView,
    WorkerListView,
    PositionListView, TaskTypeListView, TaskCreateView, TaskDetailView, assign_to_task
)

urlpatterns = [
    path("", home, name="home"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/assign/", assign_to_task, name="task-assign"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("task_type/", TaskTypeListView.as_view(), name="task-type-list"),
]

app_name = "tasks"
