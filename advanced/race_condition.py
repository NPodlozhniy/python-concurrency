import sys
from threading import Thread

# context switching frequency
sys.setswitchinterval(0.001)

counter = 0

num = 50000
n_loop = 30


def increment():
    global counter
    for _ in range(num):
        counter += 1


threads = []


def run():
    for _ in range(n_loop):
        t = Thread(target=increment)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("expected counter value = %d" % (num * n_loop))
    print("actual counter value = %d" % counter)


if __name__ == "__main__":
    run()
