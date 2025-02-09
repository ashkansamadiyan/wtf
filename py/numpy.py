import asyncio
import time

import numpy as np
import uvloop

# Use uvloop for improved performance (CPython only)
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def call_db(delay: float, i: int, results: np.ndarray):
    # Simulate an asynchronous delay
    await asyncio.sleep(delay)
    # Write the index into the preallocated numpy array at position i.
    results[i] = i


async def main():
    print("starting")
    start_time = time.time()

    n = 5_000_000
    # Preallocate a NumPy array to hold the results.
    results = np.empty(n, dtype=np.int64)

    # Create a list of 5 million tasks.
    tasks = [asyncio.create_task(call_db(3.0, i, results)) for i in range(n)]

    # Await all tasks to finish.
    await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    print(f"{elapsed} seconds")
    # Optionally inspect results:
    # print(results)


if __name__ == "__main__":
    asyncio.run(main())
