from django.urls import path, include

from tasks.views import (
    home,
    TaskListView,
    WorkerListView,
    PositionListView,
    TaskTypeListView,
    TaskCreateView,
    TaskDetailView,
    assign_to_task,
    TaskUpdateView,
    mark_completed,
    WorkerDetailView,
    TaskTypeUpdateView,
)

urlpatterns = [
    path("", home, name="home"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/assign/", assign_to_task, name="task-assign"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/mark_completed", mark_completed, name="task-mark-completed"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("task_type/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task_type/update/", TaskTypeUpdateView.as_view(), name="task-type-update")
]

app_name = "tasks"
