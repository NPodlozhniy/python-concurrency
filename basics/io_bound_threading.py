from threading import Thread

from functions import io_bound, timing, chunks


def run_sync():
    for i in range(1 << 3):
        io_bound(n=i)


def run_async():
    """
    Run func in threading mode
    """
    tasks = []
    for each in chunks(range(1 << 10), 1 << 7):
        for i in each:
            # create the thread
            t = Thread(target=io_bound, args=(i,))
            # start the thread
            t.start()
            tasks.append(t)
        for every in tasks:
            # wait for thread to finish
            every.join()


@timing
def run():
    # run_sync()
    run_async()


if __name__ == "__main__":
    run()
