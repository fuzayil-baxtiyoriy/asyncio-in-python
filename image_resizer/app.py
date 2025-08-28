import asyncio
import aiohttp
import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from PIL import Image




# Directories
IMAGES_DIR = Path("images")
RESIZED_DIR = Path("resized")
IMAGES_DIR.mkdir(exist_ok=True)
RESIZED_DIR.mkdir(exist_ok=True)

# Example image URLs
urls = [
    'https://picsum.photos/id/2/400/300',
    'https://picsum.photos/id/14/500/500',
    'https://picsum.photos/id/110/800/600',
    'https://picsum.photos/id/116/1200/800'
]

# I/O-bound: Download images
async def download_image(session, url, idx):
    try:
        async with session.get(url) as response:
            data = await response.read()
            filepath = IMAGES_DIR / f"image_{idx}.jpg"
            with open(filepath, "wb") as f:
                f.write(data)
            print(f"Downloaded {url} to {filepath}")
            return filepath
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

async def download_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, idx) for idx, url in enumerate(urls)]
        return await asyncio.gather(*tasks)


# CPU-bound: Resize images
def resize_image(filepath, size=(200, 200)):
    try:
        img = Image.open(filepath)
        img = img.resize(size)
        new_path = RESIZED_DIR / filepath.name
        img.save(new_path)
        print(f"Resized image saved to {new_path}")
        return new_path
    except Exception as e:
        print(f"Error resizing {filepath}: {e}")
        return None

async def resize_all(filepaths):
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        tasks = [loop.run_in_executor(pool, resize_image, filepath) for filepath in filepaths if filepath]
        return await asyncio.gather(*tasks)


async def main():
    print("📥 Downloading images...")
    downloaded_files = await download_all(urls)
    print("📏 Resizing images...")
    resized_files = await resize_all(downloaded_files)

    print("\n✅ Done!")
    print("Resized images:", resized_files)


if __name__ == "__main__":
    asyncio.run(main())