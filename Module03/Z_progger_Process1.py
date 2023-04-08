import multiprocessing
import time


def test():
    print("Процесс запущен")
    for _ in range(7):
        print(f"{multiprocessing.current_process()}", time.time())
        time.sleep(1)


if __name__ == "__main__":
    pr = multiprocessing.Process(target=test, name="Process-1")
    pr.start()

    i = 1
    while i <= 3:
        print("La la la - MAIN PROCESS")
        time.sleep(1)
        i += 1
    print("END OF MAIN")
    pr.join()  # МЫ не можем опуститься ниже данной строчки кода пока наш процесс этот не будет завершен!Для теста комментируй эту строку и смотри как меняется вывод.
    print("All is end")
    print("All is end")
    print("All is end")
