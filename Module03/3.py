from threading import Thread
from time import sleep
import logging


class UsefulClass:
    def __init__(self, second_num):
        self.delay = second_num

    def __call__(self):
        sleep(self.delay)
        logging.debug("Wake up!")


if __name__ == "__main__":

    logging.basicConfig(
        format="%(asctime)s %(threadName)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
        handlers=[logging.FileHandler("program.log"), logging.StreamHandler()],
    )
    t2 = UsefulClass(2)
    t3 = UsefulClass(5)
    thread = Thread(target=t2)
    thread1 = Thread(target=t3)
    thread.start()
    thread1.start()
    print("Some stuff")
