from django.test import TestCase
from tasklist.home.models import Task
from datetime import date

class TaskFilterTestCase(TestCase):
    def setUp(self):
        # Create some sample tasks
        Task.objects.create(title="Task 1", status="To Do",due_date=date.today())
        Task.objects.create(title="Task 2", status="In Progress",due_date=date.today())
        Task.objects.create(title="Task 3", status="Done",due_date=date.today())

    def test_filter_by_status(self):
        filtered_pending_tasks = Task.objects.filter(status="To Do")
        filtered_completed_tasks = Task.objects.filter(status="In Progress")

        # Assert that the correct tasks are filtered
        self.assertEqual(filtered_pending_tasks.count(), 1)
        self.assertEqual(filtered_completed_tasks.count(), 1)


class TaskSortingTestCase(TestCase):
    def setUp(self):
        # Create some sample tasks with different priorities
        Task.objects.create(title="Task A", priority=1,due_date=date.today())
        Task.objects.create(title="Task B", priority=2,due_date=date.today())
        Task.objects.create(title="Task C", priority=3,due_date=date.today())

    def test_sort_by_priority(self):
        sorted_tasks = Task.objects.order_by('priority')

        # Assert that tasks are sorted in the expected order of priority
        self.assertEqual(sorted_tasks[2].name, "Task C")
        self.assertEqual(sorted_tasks[1].name, "Task B")
        self.assertEqual(sorted_tasks[0].name, "Task A")


