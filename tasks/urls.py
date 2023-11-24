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
    TaskTypeUpdateView, TaskTypeCreateView, TaskTypeDeleteView, PositionCreateView, PositionUpdateView,
    PositionDeleteView, TaskDeleteView, WorkerCreateView, WorkerUpdateView, WorkerDeleteView,
)

urlpatterns = [
    path("", home, name="home"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/assign/", assign_to_task, name="task-assign"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/mark_completed", mark_completed, name="task-mark-completed"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/create/", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("position/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
    path("task_type/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task_type/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path(
        "task_type/<int:pk>/delete",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete"
    ),
    path(
        "task_type/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update"
    )
]

app_name = "tasks"
