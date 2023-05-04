import redis
import timeit
from redis_lru import RedisLRU

# создание объекта Redis и LRU-кэша с максимальным размером 3 элемента
client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client, default_ttl=1, max_size=3)

# рекурсивное вычисление чисел Фибоначчи
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# декоратор для кэширования результатов функции fibonacci_with_cache
@cache
def fibonacci_with_cache(n):
    """Returns the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)


# проверка работоспособности функций fibonacci и fibonacci_with_cache
if __name__ == "__main__":
    # вычисление 35-го числа Фибоначчи без кэширования
    start_time_1 = timeit.default_timer()
    fib_1 = fibonacci(35)
    print(f"Time 1 was:{timeit.default_timer() - start_time_1}")
    print(fib_1)

    # вычисление 235-го числа Фибоначчи с использованием кэша
    start_time_2 = timeit.default_timer()
    fib_2 = fibonacci_with_cache(235)
    print(f"Time 2 was:{timeit.default_timer() - start_time_2}")
    print(fib_2)
