'''
Thread-based race condition demo
Implemented with doctest
'''
import logging
import threading
import time

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO)


def main(num_threads: int, num_increments: int):
  """Demonstrates race condition in simple multithreaded update of a counter

    >>> main(num_threads=1, num_increments=10000)
    10000

    >>> main(num_threads=10, num_increments=1000)
    10000

    >>> main(num_threads=100, num_increments=100)
    10000

    >>> main(num_threads=1000, num_increments=10)
    10000

    >>> main(num_threads=10000, num_increments=1)
    10000
    """

  counter = 0

  def increment_counter(increments: int):
    """A function to increment a shared counter
        """
    nonlocal counter  # tells Python that the `counter` variable is not local to this function

    for _ in range(increments):
      curr_val = counter
      time.sleep(0)  # a tiny delay between the read and write
      counter = curr_val + 1

  # create `num_threads` new threads using the `increment_counter` function
  threads = [
      threading.Thread(target=increment_counter, args=(num_increments,))
      for _ in range(num_threads)
  ]

  # start the threads as fast as we can
  for thread in threads:
    thread.start()

  # wait for the threads to complete
  for thread in threads:
    thread.join()

  # return the final value of the `counter` shared variable
  return counter


if __name__ == '__main__':
  import doctest
  doctest.testmod()
