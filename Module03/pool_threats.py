import concurrent.futures
import logging
from random import randint
from time import sleep


def greeting(name):
    logging.debug(f"greeting for: {name}")
    sleep(2)
    print(f"Hello {name}")


arguments = ("Bill", "Jill", "Till", "Sam", "Tom", "John", "PIDOR!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(greeting, arguments)

    logging.debug("Finish")
