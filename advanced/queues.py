import queue
from threading import Thread
from time import sleep

q = queue.Queue()


def some_setup_process():
    """
    create database connections and ...
    """
    print("i am going to create the setup", flush=True)
    sleep(3)
    print("i've done setting up")
    q.put("lock")


def worker():
    print("i am doing something not important", flush=True)
    # it needs to make sure the setup process in finished
    q.get()  # wait until another thread don't put something to queue
    print("i am inserting data", flush=True)


tasks = []

for each in (worker, some_setup_process):
    t = Thread(target=each)
    t.start()
    tasks.append(t)

for t in tasks:
    t.join()
