from django.urls import path, include

from tasks.views import (
    home,
    TaskListView,
    WorkerListView,
    PositionListView,
)

urlpatterns = [
    path("", home, name="home"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("position/", PositionListView.as_view(), name="position-list")
]

app_name = "tasks"
