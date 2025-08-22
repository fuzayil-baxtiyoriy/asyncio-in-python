import asyncio
import time
from delay import delay
from utils import async_timed

# async function to run tasks concurrently

@async_timed()
async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_once_more

# start = time.perf_counter()
asyncio.run(main())
# end = time.perf_counter()
# print(f"Program finished in {end - start:.2f} seconds")