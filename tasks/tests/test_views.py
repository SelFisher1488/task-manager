from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from tasks.models import TaskType, Task, Position
from datetime import datetime

TASK_TYPE_URL = reverse("tasks:task-type-list")
TASK_URL = reverse("tasks:task-list")
POSITION_URL = reverse("tasks:position-list")
WORKER_URL = reverse("tasks:worker-list")


class PublicTests(TestCase):
    def test_tasktype_login_required(self):
        res = self.client.get(TASK_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_worker_login_required(self):
        res = self.client.get(WORKER_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_task_login_required(self):
        res = self.client.get(TASK_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_position_login_required(self):
        res = self.client.get(POSITION_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTests(TestCase):

    def setUp(self) -> None:
        self.position = Position.objects.create(name="testpos")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            position=self.position
        )
        self.client.force_login(self.user)

    def test_retrieve_tasks(self):
        Task.objects.create(
            name="tesk1",
            description="testtesttesttest",
            deadline=datetime.now().date(),
            priority="2",
            task_type=TaskType.objects.create(name="testt")
        )
        Task.objects.create(
            name="tesk2",
            description="testesttesttestetst",
            deadline=datetime.now().date(),
            priority="3",
            task_type=TaskType.objects.create(name="testtt")
        )

        response = self.client.get(TASK_URL)
        task_list = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(task_list)
        )
        self.assertTemplateUsed(
            response,
            "tasks/task_list.html"
        )

    def test_search_form(self):
        response = self.client.get(TASK_URL)
        form = response.context["search_form"]

        self.assertEqual(form.initial["name"], "")


class PrivateWorkerTests(TestCase):

    def setUp(self) -> None:
        self.position = Position.objects.create(name="testpos")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            position=self.position
        )
        self.client.force_login(self.user)

    def test_retrieve_workers(self):

        get_user_model().objects.create(
            username="test11",
            first_name="test1",
            last_name="test2",
            email="test@test.com",
            position=self.position
        )
        get_user_model().objects.create(
            username="test3",
            first_name="test4",
            last_name="test5",
            email="test6@test.com",
            position=self.position
        )

        response = self.client.get(WORKER_URL)
        worker_list = get_user_model().objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["worker_list"]),
            list(worker_list)
        )
        self.assertTemplateUsed(
            response,
            "tasks/worker_list.html"
        )

    def test_search_form(self):
        response = self.client.get(WORKER_URL)
        form = response.context["search_form"]

        self.assertEqual(form.initial["username"], "")


class PrivateTaskTypeTests(TestCase):

    def setUp(self) -> None:
        self.position = Position.objects.create(name="testpos")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            position=self.position
        )
        self.client.force_login(self.user)

    def test_retrieve_tasktype(self):
        TaskType.objects.create(name="testt")
        TaskType.objects.create(name="testtt")
        response = self.client.get(TASK_TYPE_URL)
        task_type_list = TaskType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_type_list"]),
            list(task_type_list)
        )
        self.assertTemplateUsed(
            response,
            "tasks/task_type_list.html"
        )

    def test_search_form(self):
        response = self.client.get(TASK_TYPE_URL)
        form = response.context["search_form"]

        self.assertEqual(form.initial["name"], "")


class PrivatePositionTests(TestCase):

    def setUp(self) -> None:
        self.position = Position.objects.create(name="testpos")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            position=self.position
        )
        self.client.force_login(self.user)

    def test_retrieve_positions(self):
        Position.objects.create(name="testt")
        Position.objects.create(name="testtt")

        response = self.client.get(POSITION_URL)
        position_list = Position.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]),
            list(position_list)
        )
        self.assertTemplateUsed(
            response,
            "tasks/position_list.html"
        )

    def test_search_form(self):
        response = self.client.get(POSITION_URL)
        form = response.context["search_form"]

        self.assertEqual(form.initial["name"], "")
