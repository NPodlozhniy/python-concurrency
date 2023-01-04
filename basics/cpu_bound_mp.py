from functions import cpu_bound, timing
from multiprocessing import Process, cpu_count
from multiprocessing import Pool

NUMBER = 30

def run_sync():
    for i in [NUMBER] * 12:
        cpu_bound(i)


def run_async1():
    jobs = []
    for i in range(cpu_count()):
        # create the process
        p = Process(target=cpu_bound, args=(NUMBER,))
        # start it
        p.start()
        jobs.append(p)
    for each in jobs:
        # wait for it
        each.join()


def run_async2():
    """
    Better approach to avoid CPU's overloading
    """
    promises = []
    final = []
    with Pool(cpu_count() // 2) as handler:
        for i in [NUMBER] * 12:
            r = handler.apply_async(cpu_bound, [i])
            promises.append(r)
        for r in promises:
            final.append(r.get())
    print(final, flush=True)


@timing
def run():
    # run_sync()
    run_async2()


if __name__ == "__main__":
    run()
