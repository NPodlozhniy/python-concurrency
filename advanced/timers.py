from sched import scheduler
from threading import Thread, Timer
from time import sleep

DELAY = 3


def run_later(message: str) -> None:
    for i in range(DELAY, 0, -1):
        print("%d.." % i, flush=True, end=" ")
        sleep(1)  # the most popular way to implement timer
    print(message, flush=True)


print("Let's wait a bit!", flush=True)

# more sophisticated way
timer = Timer(DELAY, run_later, kwargs={"message": "Hello, world!"})
timer.start()

sleep(DELAY)  # ignored by timer

timer.join()

# fascinated way to implement full-fledged planning
s = scheduler()
s.enter(DELAY, 1, run_later, kwargs={"message": "Cool, i am a winner)"})
s.enter(DELAY, 2, run_later, kwargs={"message": "Shit, i am a loser("})

print("\nI am about to execute a scheduler", flush=True)

t = Thread(target=s.run)
t.start()

sleep(DELAY)  # ignored by scheduler

t.join()
