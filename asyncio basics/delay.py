import asyncio, time
from utils import async_timed   

@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f"sleeping for {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} seconds")
    return delay_seconds

def delay_sync(delay_seconds: int) -> int:
    print(f"sleeping for {delay_seconds} seconds")
    time.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} seconds")
    return delay_seconds