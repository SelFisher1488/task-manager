from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from tasks.forms import TaskForm
from tasks.models import Worker, Task, Position, TaskType


@login_required
def home(request) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_positions = Position.objects.count()
    num_task_types = TaskType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_positions": num_positions,
        "num_task_types": num_task_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "tasks/home.html", context=context)


@login_required
def assign_to_task(request, pk) -> HttpResponseRedirect:
    worker = Worker.objects.get(id=request.user.id)
    if Task.objects.get(id=pk) in worker.tasks.all():
        worker.tasks.remove(pk)
    else:
        worker.tasks.add(pk)
    return HttpResponseRedirect(reverse_lazy("tasks:task-detail", args=[pk]))


@login_required
def mark_completed(request, pk) -> HttpResponseRedirect:
    task = Task.objects.get(id=pk)
    task.is_completed = True
    task.complete_date = timezone.now()
    task.save()
    return HttpResponseRedirect(reverse_lazy("tasks:task-list"))


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task:tasktype-list")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = Task.objects.all().prefetch_related("assignees")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy("tasks:task-detail", args=[self.object.pk])


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 5


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.all().prefetch_related("tasks")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position

