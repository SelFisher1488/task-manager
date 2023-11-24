from django.test import TestCase
from tasks.forms import TaskTypeSearchForm, WorkerForm, PositionSearchForm
from tasks.models import Position
from django.contrib.auth import get_user_model


class FormsTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="testpos")
        self.user_model = get_user_model()
        self.worker = self.user_model.objects.create_user(
            username="test",
            first_name="test1",
            last_name="test2",
            email="test@test.com",
            position=self.position,
        )

    def test_worker_form_valid(self):
        form_data = {
            "username": "ntest",
            "first_name": "ntest1",
            "last_name": "ntest2",
            "email": "test1@test.com",
            "position": self.position.id,
            "password1": "test12345",
            "password2": "test12345",
        }
        form = WorkerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_form_invalid(self):
        form_data = {
            "username": "ntest",
            "first_name": "ntest1",
            "last_name": "ntest2",
            "email": "test1@test.com",
            "password1": "test12345",
            "password2": "test12345",
        }
        form = WorkerForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_type_search_form_valid(self):
        form_data = {"name": "testt"}
        form = TaskTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_position_search_form_valid(self):
        form_data = {"name": "testpos"}
        form = PositionSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
