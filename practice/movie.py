import os
import random
import sys
import time
from subprocess import PIPE, Popen
from threading import Thread

COMMAND = """ffmpeg -r 24 -i movie.mp4 -vf drawtext="fontfile=hyped.ttf: \
        textfile=text.txt: fontcolor=black: fontsize=64: box=1: boxcolor=teal@0.75: \
        boxborderw=8: x=(w-text_w)/2: y=h/2:reload=1" -codec:a copy -r 24 output.mp4"""

TEXT = "".join(
    random.choice((str.upper, str.lower))(char) for char in "What a great hole! Scary!"
)


def textwriter(text: str) -> None:
    open("text.txt", "w").close()
    time.sleep(0.25)
    with open("text.txt", "w") as handler:
        for c in text:
            time.sleep(random.random() / 2)
            handler.write(c)
            handler.flush()


def execute(cmd: str):
    p = Popen(cmd, stderr=PIPE, bufsize=128, universal_newlines=True, shell=True)
    for line in iter(p.stderr.readline, ""):
        if p.poll():
            break
        yield line
    p.wait()


if os.path.isfile("output.mp4"):
    os.remove("output.mp4")

# start the text writer
t = Thread(target=textwriter, args=(TEXT,))
t.start()

# start the external shell
for _each in execute(COMMAND):
    print(">", flush=True, end="")

# wait for all
t.join()

# open the final movie
os.system("start output.mp4")
