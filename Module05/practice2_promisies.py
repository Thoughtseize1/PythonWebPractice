import asyncio
from asyncio import Future


async def make_request(x):
    # print(f"DO REQUEST IN DATABASE {x}")
    await asyncio.sleep(1)


async def main():
    chunk = 200
    tasks = []
    pended = 0
    for x in range(10_000):
        tasks.append(asyncio.create_task(make_request(x)))
        pended += 1
        if len(tasks) == chunk or pended == 10000:
            await asyncio.gather(*tasks)
            tasks.clear()
            print(pended)
        # await asyncio.gather(task)


if __name__ == "__main__":
    asyncio.run(main())
# Ниже, тоже самое, только создавая Event loop
# loop = asyncio.new_event_loop()
# loop.run_until_comple te(main())
