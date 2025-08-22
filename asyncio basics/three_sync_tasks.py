import asyncio
import time
from delay import delay_sync

# async function to run tasks concurrently
def main():
    sleep_for_three = delay_sync(3)
    sleep_again = delay_sync(3)
    sleep_once_more = delay_sync(3)

start = time.perf_counter()
main()
end = time.perf_counter()
print(f"Program finished in {end - start:.2f} seconds")

