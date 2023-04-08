from threading import (
    Thread,
    BoundedSemaphore,
    Semaphore,
    current_thread,
    active_count,
    enumerate,
)
import time
import random

max_connections = 3
pool = BoundedSemaphore(value=max_connections)


def test():
    slp = random.randint(1, 2)
    with pool:
        print(f"{current_thread().name} + ({slp})")
        time.sleep(slp)


for i in range(27):
    a = Thread(target=test, name=f"PidoR-{i}")
    a.start()

while True:
    print("Active thread: ", active_count())
    print("Enumerate: ", len(enumerate()))
    time.sleep(1)
