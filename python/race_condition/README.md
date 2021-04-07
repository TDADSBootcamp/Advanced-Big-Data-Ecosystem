A demonstration of a race condition.

# Description

- A counter variable `counter` is initialised to zero.
- A function `increment_counter` is created that increments that variable a specified number of times
  - A `time.sleep(0)` call occurs between reading the value and writing the incremented value back. That creates a tiny delay between the read and write. 
- `main` takes an argument `num_threads` and creates that number of threads, each executing the `increment_counter` function. It also takes `num_increments` which is passed to each thread and determines how many times it tries to imcrement the value.

# Execution

`pipenv run python python/race_condition/race_demo.py`

This will run the `doctest`s defined for the `main` function, demonstrating the final counter value under a range of `num_threads` and `num_increments` values. Each example asswers the correct `counter` value if there was no race condition. Those tests that pass do not print anything.

## Typical Output

```python
**********************************************************************
File "python/race_condition/race_demo.py", line 13, in __main__.main
Failed example:
    main(num_threads=10, num_increments=1000)
Expected:
    10000
Got:
    1158
```

# Notes

Without the `sleep(0)`, is it still possible to trigger the race condition. Use larger values for `num_threads` and `num_increments`.