import asyncio
import time

start = time.perf_counter()
async def cpu_heavy():
    sum(range(10**8))
    print("CPU-heavy task completed")

async def main():
    await asyncio.gather(cpu_heavy(), cpu_heavy(), cpu_heavy())


asyncio.run(main())
end = time.perf_counter()
print(f"Program finished in {end - start:.2f} seconds")