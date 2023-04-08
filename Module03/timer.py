from threading import Thread
import logging
from time import sleep, time

value = 5


def example_work(params):
    sleep(params)
    logging.debug("Wake up!")
    global value
    value += 1


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    logging.debug("Start program")
    start = time()
    threads = []

    for i in range(5):
        thread = Thread(target=example_work, args=(i,))
        thread.start()
        thread.join()
        threads.append(thread)

    # [el.join() for el in threads]
    end = time() - start

    logging.debug(f"End program with {end} + {value}")
