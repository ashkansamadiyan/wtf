import asyncio
import time

import numpy as np
import uvloop

# Use uvloop for improved performance (CPython only)
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def call_db(delay: float, i: int, results: np.ndarray):
    await asyncio.sleep(delay)
    results[i] = i


async def main():
    print("starting")
    start_time = time.time()

    n = 5_000_000
    results = np.empty(n, dtype=np.int64)

    tasks = [asyncio.create_task(call_db(3.0, i, results)) for i in range(n)]

    # Await all tasks to finish.
    await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    print(f"{elapsed} seconds")
    # print(results)


if __name__ == "__main__":
    asyncio.run(main())
