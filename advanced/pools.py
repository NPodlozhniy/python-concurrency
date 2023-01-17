from concurrent.futures import ThreadPoolExecutor
from time import sleep


def print_after_sec(message):
    sleep(1)
    print(message, flush=True)
    return "WoW"


with ThreadPoolExecutor(max_workers=3) as pool:
    future = []
    for i in range(10):
        # print phrases in triplets as soon as max_workers is 3
        task = pool.submit(print_after_sec, (f"Hello, world {i}!"))
        future.append(
            task
        )
        print(task.done())

for task in future:
    try:
        print(task.result(), flush=True)
    except Exception as e:
        print(e, flush=True)
