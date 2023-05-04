import redis
from redis_lru import RedisLRU

r = redis.Redis(host="localhost", port=6379, password=None)

r.set("foo", "bar")
value = r.get("foo")
print(value.decode())  # bar


client = redis.StrictRedis(
    host="localhost", port=6379, username="default", password=None
)

#! 1 minute for cache using default_ttl parametr
cache = RedisLRU(client, default_ttl=1, max_size=3)


@cache
def f(x):
    print(f"Function call f({x})")
    return x


if __name__ == "__main__":
    print(f"Result f(3): {f(3)}")
    print(f"Result f(3): {f(3)}")
    print(f"Result f(4): {f(4)}")
    print(f"Result f(4): {f(4)}")
    cache.clear_all_cache()
