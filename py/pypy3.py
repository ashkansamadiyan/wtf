import asyncio
import time


async def call_db(delay, i, results):
    # Simulate the delay asynchronously.
    await asyncio.sleep(delay)
    results.append(i)


async def main():
    print("starting")
    start_time = time.time()

    # Use a standard Python list to collect results.
    results = []

    # Spawn 5 million tasks.
    tasks = [asyncio.create_task(call_db(3, i, results)) for i in range(5_000_000)]
    await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    print(f"{elapsed} seconds")
    # Optionally inspect results:
    # print(results)


if __name__ == "__main__":
    asyncio.run(main())
