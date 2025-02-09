import asyncio
import time

import uvloop

# Use uvloop as the default event loop for enhanced performance.
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def call_db(delay: float, i: int, results: list):
    # Simulate a delay (e.g. a database call)
    await asyncio.sleep(delay)
    # Append the index to the results list.
    results.append(i)


async def main():
    print("starting")
    start_time = time.time()

    results = []  # Shared results list
    # Prepare a list of tasks. Each task will wait for `delay` seconds
    # and then add its index to the results.
    tasks = [asyncio.create_task(call_db(3, i, results)) for i in range(5_000_000)]

    # Await all tasks to finish.
    await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    print(f"{elapsed} seconds")
    # Optionally inspect the results:
    # print(results)


if __name__ == "__main__":
    asyncio.run(main())
