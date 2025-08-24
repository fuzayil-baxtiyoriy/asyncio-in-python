from concurrent.futures import ProcessPoolExecutor
import asyncio
import time

start = time.perf_counter()
def cpu_heavy_task(n):
    sum(range(n))
    print("CPU-heavy task completed")

async def main():
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as pool:
        tasks  = [
            loop.run_in_executor(pool, cpu_heavy_task, 10**8),
            loop.run_in_executor(pool, cpu_heavy_task, 10**8),
            loop.run_in_executor(pool, cpu_heavy_task, 10**8)
        ]
        results = await asyncio.gather(*tasks)
        print(results)

if __name__ == "__main__":
    asyncio.run(main())
    end = time.perf_counter()
    print(f"Program finished in {end - start:.2f} seconds")