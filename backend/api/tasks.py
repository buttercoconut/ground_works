"""Celery task definitions for the Ground Works backend.

A simple example task is provided that simulates a long‑running boring
operation.  The task can be called from the API or from other services.
"""

from celery import shared_task
import time

@shared_task
def boring_operation(task_id: int, duration: int = 5) -> str:
    """Simulate a boring operation that takes ``duration`` seconds.

    Parameters
    ----------
    task_id: int
        Identifier of the task being processed.
    duration: int, optional
        Number of seconds to sleep.  Defaults to 5.

    Returns
    -------
    str
        A simple status message.
    """
    time.sleep(duration)
    return f"Task {task_id} completed after {duration} seconds"
