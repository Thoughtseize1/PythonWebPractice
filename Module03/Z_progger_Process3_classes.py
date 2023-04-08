import multiprocessing
import time


class Process(multiprocessing.Process):
    def run(self):
        print("I'm WORKING")


if __name__ == "__main__":
    pr = Process()
    pr.start()
