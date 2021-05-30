import time


def busy_wait(delay: float):
  """Busy wait.

  Args:
    delay: Time to wait in seconds.
  """
  start = time.time()
  while time.time() - start < delay:
      pass
  return