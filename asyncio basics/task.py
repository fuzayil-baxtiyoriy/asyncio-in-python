import asyncio

from delay import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = sleep_for_three
    print(f"Result: {result}")

asyncio.run(main())