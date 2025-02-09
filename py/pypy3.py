import asyncio
import time


async def call_db(delay, i, results):
    await asyncio.sleep(delay)
    results.append(i)


async def main():
    print("starting")
    start_time = time.time()

    results = []

    tasks = [asyncio.create_task(call_db(3, i, results)) for i in range(5_000_000)]
    await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    print(f"{elapsed} seconds")
    # print(results)


if __name__ == "__main__":
    asyncio.run(main())
