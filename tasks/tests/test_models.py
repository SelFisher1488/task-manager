from datetime import datetime, date

from django.contrib.auth import get_user_model
from django.test import TestCase

from tasks.models import TaskType, Position, Task


class ModelsTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="testt")
        self.position = Position.objects.create(name="testpos")
        self.user = get_user_model().objects.create(
            username="test",
            password="test12345",
            first_name="test1",
            last_name="test2",
            position=self.position
        )
        self.task = Task.objects.create(
            name="tesk",
            description="testsetsetst",
            deadline=datetime.now().date(),
            is_completed=False,
            priority="4",
            task_type=self.task_type,
        )
        self.task2 = Task.objects.create(
            name="tesk2",
            description="testsetsetsetest",
            deadline=date(2022, 12, 23),
            is_completed=False,
            priority="4",
            task_type=self.task_type,
        )

    def test_check_time(self):
        self.assertTrue(self.task.check_deadline())
        self.assertFalse(self.task2.check_deadline())

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "testt")

    def test_task_str(self):
        self.assertEqual(
            str(self.task), f"tesk better to do by: {self.task.deadline}"
        )

    def test_position_str(self):
        self.assertEqual(str(self.position), "testpos")

    def test_worker_str(self):
        self.assertEqual(str(self.user), "test1 test2 (position: testpos)")
