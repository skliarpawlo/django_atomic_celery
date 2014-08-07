from django.db import transaction
from django.db.transaction import atomic
from django.test import TransactionTestCase
from django_atomic_celery import PostTransactionTask


class TaskTestCase(TransactionTestCase):
    """Test case for tasks.
    """

    def test_delay(self):
        """@task(..).delay(..)
        """

        with transaction.atomic():
            print("Inside main atomic")
            MyPostAtomicTask.delay()


class MyPostAtomicTask(PostTransactionTask):
    def run(*args, **kwargs):
        with atomic():
            print("What if post atomic task is itself atomic, ha?")
