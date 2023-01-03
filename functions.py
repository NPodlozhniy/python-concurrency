import time
import sys

# copy info from wrapped func to wrapper func
from functools import wraps


def cprint(statement, debug: bool=True, end="\n") -> None:
    print(statement, file=sys.stderr if debug else sys.stdout, flush=True, end=end)


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        cprint(f"function <{func.__name__}> took: {te-ts:.2f} seconds")
        return result
    return wrapper


def io_bound(n: int) -> None:
    """
    When the most time is spent on waiting for Input/Output operations to be completed
    For example:
        - network operations
        - disk operation
        - any other resource related operation (except CPU!)
    """
    time.sleep(2)
    fpath = "tmp_io_bound.txt"
    open(fpath, "w").close() # clean the file
    cprint(f"I am about to start task number {n}")
    with open(fpath, "w") as handler:
        for i in range(10):
            handler.write("0" * (1 << 20))
            handler.flush()
    cprint(f"I've finished task number {n}")


def cpu_bound(n: int) -> int:
    """
    When the time to complete a task is determined by the CPU speed
    """
    if n < 2:
        return 1
    else:
        return cpu_bound(n - 1) + cpu_bound(n - 2)


def chunks(lst: list, n: int) -> list:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i+n]
