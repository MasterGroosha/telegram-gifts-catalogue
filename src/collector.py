import asyncio
import shutil
from datetime import datetime, timezone
from json import dumps
from os import getenv
from pathlib import Path

from aiogram import Bot
from aiogram.types import Gift, Gifts
import logging

BASE_OUTPUT_DIR = Path("/tmp/gifts")
IMAGES_DIR = BASE_OUTPUT_DIR.joinpath("images")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def prepare_dirs():
    """
    Create necessary directories and copy static files.
    """
    for output_dir in (BASE_OUTPUT_DIR, IMAGES_DIR):
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
    for filename in ("index.html", "style.css"):
        shutil.copyfile(src=f"web/{filename}", dst=BASE_OUTPUT_DIR.joinpath(f"{filename}"))

def update_date():
    """
    Update the date in the HTML file to the current date and time.
    """
    html_file = BASE_OUTPUT_DIR.joinpath("index.html")
    current_date = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(html_file, "r") as f:
        content = f.read()

    updated_content = content.replace("%DATE%", current_date)
    with open(html_file, "w") as f:
        f.write(updated_content)

async def download_gifts(bot: Bot):
    """
    Download available gifts and save their data and images.

    Parameters:
    bot (Bot): An instance of the aiogram Bot.
    """
    data = []
    try:
        available_gifts: Gifts = await bot.get_available_gifts()
    except Exception as e:
        logger.error(f"Failed to fetch available gifts: {e}")
        return

    # Process available gifts
    for index, gift in enumerate(available_gifts.gifts):
        data.append({
            "id": gift.id,
            "price": gift.star_count,
            "upgrade_price": gift.upgrade_star_count,
            "remaining_count": gift.remaining_count,
            "total_count": gift.total_count,
        })
        file_name = f"{gift.id}.tgs"
        destination_dir = IMAGES_DIR
        try:
            await bot.download(file=gift.sticker.file_id, destination=destination_dir.joinpath(file_name).absolute())
            logger.info(f"Downloaded available gift {index + 1}/{len(available_gifts.gifts)}")
        except Exception as e:
            logger.error(f"Failed to download available gift {gift.id}: {e}")
        await asyncio.sleep(1)

    with open(BASE_OUTPUT_DIR.joinpath("data.json"), "w") as f:
        f.write(dumps(data, indent=4))

async def main():
    """
    Main function to prepare directories, update date, and download gifts.
    """
    prepare_dirs()
    update_date()
    async with Bot(token=getenv("BOT_TOKEN")) as bot:
        await download_gifts(bot)

if __name__ == '__main__':
    asyncio.run(main())
