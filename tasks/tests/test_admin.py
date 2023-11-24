from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.test import TestCase
from tasks.admin import WorkerAdmin, TaskTypeAdmin, PositionAdmin, TaskAdmin
from tasks.models import Worker, TaskType, Position, Task


class AdminTests(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.worker_admin = WorkerAdmin(Worker, self.site)
        self.task_type_admin = TaskTypeAdmin(TaskType, self.site)
        self.position_admin = PositionAdmin(Position, self.site)
        self.task_admin = TaskAdmin(Task, self.site)
        self.position = Position.objects.create(name="testpos")
        self.worker = get_user_model().objects.create_user(
            username="test",
            first_name="test1 ",
            last_name="test2",
            email="test@test.com",
            position=self.position,
        )

    def test_worker_admin_fieldsets(self):
        user_admin_fieldsets = UserAdmin.fieldsets
        additional_info_fields = ("position",)
        expected_fieldsets = user_admin_fieldsets + (
            ("Additional info", {"fields": additional_info_fields}),
        )
        self.assertEqual(self.worker_admin.fieldsets, expected_fieldsets)

    def test_worker_position_listed(self):
        worker_from_db = Worker.objects.get(username="test")
        self.assertEqual(worker_from_db.position, self.position)

    def test_worker_admin_list_display(self):
        expected_list_display = UserAdmin.list_display + ("position",)
        self.assertEqual(self.worker_admin.list_display, expected_list_display)

    def test_worker_admin_list_filter(self):
        user_admin_filters = UserAdmin.list_filter
        expected_list_filter = user_admin_filters + ("position",)
        self.assertEqual(self.worker_admin.list_filter, expected_list_filter)
