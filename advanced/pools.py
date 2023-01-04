from concurrent.futures import ThreadPoolExecutor
from time import sleep


def print_after_sec(message):
    sleep(1)
    print(message, flush=True)
    return "WoW"


with ThreadPoolExecutor(max_workers=3) as pool:
    for i in range(10):
        # print phrases in triplets as soon as max_workers is 3
        future = pool.submit(print_after_sec, ("Hello, world!"))
        print(future.done())

print(future.result())
