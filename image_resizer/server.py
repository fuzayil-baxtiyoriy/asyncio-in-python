import asyncio
import time
from app import download_all, resize_all_parallel, urls, resize_all_sequential


async def main():
    print("📥 Downloading images...")
    downloaded_files = await download_all(urls)
    print("📏 Resizing images...")
    resized_files = await resize_all_parallel(downloaded_files)

    print("\n✅ Done!")
    print("Resized images:", resized_files)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")

# In Parallel takes Total time: 39.98 seconds
# In Sequential takes Total time: 34.62 seconds