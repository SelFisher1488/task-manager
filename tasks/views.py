from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from tasks.forms import (
    TaskForm,
    TaskSearchForm,
    TaskTypeSearchForm,
    WorkerForm,
    WorkerSearchForm,
    PositionSearchForm,
)
from tasks.models import (
    Worker,
    Task,
    TaskType,
    Position,
)


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


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypeListView, self).get_context_data()
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskTypeSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = TaskType.objects.all()
        form = TaskTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "tasks/task_type_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(
            initial={
                "name": name
            }
        )

        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = Task.objects.prefetch_related("assignees")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(
            initial={
                "username": username
            }
        )
        return context

    def get_queryset(self):
        queryset = Worker.objects.select_related("position")
        username = self.request.GET.get("username")
        if username:
            return queryset.filter(username__icontains=username)
        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    queryset = Worker.objects.prefetch_related("tasks")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = WorkerForm
    success_url = reverse_lazy("tasks:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "position"
    )
    success_url = reverse_lazy("tasks:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("tasks:worker-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = PositionSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = Position.objects.all()
        username = self.request.GET.get("username")
        if username:
            return queryset.filter(username__icontains=username)
        return queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("tasks:position-list")
