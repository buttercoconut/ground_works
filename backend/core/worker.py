"""Celery worker configuration.

The worker is configured to use Redis as both broker and result backend.
The ``tasks`` module is imported so that Celery discovers the task
definitions.
"""

from celery import Celery

from .config import settings

celery_app = Celery(
    "ground_works",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

# Import tasks to register them with Celery
import ground_works.backend.api.tasks  # noqa: F401
