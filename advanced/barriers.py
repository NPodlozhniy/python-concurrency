from threading import Barrier, Thread
from time import sleep

b = Barrier(parties=2, timeout=30)


def some_setup_process():
    """
    create database connections and ...
    """
    print("i am going to create the setup", flush=True)
    sleep(3)
    print("i've done setting up")
    b.wait()  # remove (pass) a barrier


def worker():
    print("i am doing something not important", flush=True)
    # it needs to make sure the setup process in finished
    b.wait()  # create (release) a barrier
    print("i am inserting data", flush=True)


tasks = []

for each in (worker, some_setup_process):
    t = Thread(target=each)
    t.start()
    tasks.append(t)

for t in tasks:
    t.join()
