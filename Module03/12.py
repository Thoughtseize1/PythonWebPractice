from threading import Semaphore, Thread, active_count
import logging
from time import sleep


def worker(condition):
    with condition:
        logging.debug(f"Got semaphore")
        sleep(1)
        logging.debug(f"finished")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    pool = Semaphore(2)
    for num in range(10):
        thread = Thread(name=f"Th-{num}", target=worker, args=(pool,))
        thread.start()

while True:
    print("Active thread: ", active_count())
    sleep(1)
