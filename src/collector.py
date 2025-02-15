import asyncio
import shutil
from datetime import datetime, timezone
from json import dumps
from os import getenv
from pathlib import Path

from aiogram import Bot
from aiogram.types import Gift, Gifts

BASE_OUTPUT_DIR = Path("/Users/groosha/PycharmProjects/telegram-gifts-catalogue/website2")
IMAGES_DIR = BASE_OUTPUT_DIR.joinpath("images")

def prepare_dirs():
    for output_dir in (BASE_OUTPUT_DIR, IMAGES_DIR):
        if not output_dir.exists():
            output_dir.mkdir()
    for filename in ("index.html", "style.css"):
        shutil.copyfile(src=f"web/{filename}", dst=BASE_OUTPUT_DIR.joinpath(f"{filename}"))

def update_date():
    html_file = BASE_OUTPUT_DIR.joinpath("index.html")
    current_date = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(html_file, "r") as f:
        content = f.read()

    updated_content = content.replace("%DATE%", current_date)
    with open(html_file, "w") as f:
        f.write(updated_content)


async def download_gifts(
        bot: Bot,
):
    data = list()

    available_gifts: Gifts = await bot.get_available_gifts()
    gift: Gift
    for index, gift in enumerate(available_gifts.gifts):
        data.append({
            "id": gift.id,
            "price": gift.star_count,
            "upgrade_price": gift.upgrade_star_count,
            "remaining_count": gift.remaining_count,
            "total_count": gift.total_count,
        })
        file_name = f"{gift.id}.tgs"
        await bot.download(
            file=gift.sticker.file_id,
            destination=IMAGES_DIR.joinpath(file_name).absolute(),
        )
        print(f"Downloaded {index + 1}/{len(available_gifts.gifts)}")
        await asyncio.sleep(1)
    with open(BASE_OUTPUT_DIR.joinpath("data.json"), "w") as f:
        f.write(dumps(data))


async def main():
    prepare_dirs()
    update_date()
    async with Bot(token=getenv("BOT_TOKEN")) as bot:
        await download_gifts(bot)


if __name__ == '__main__':
    asyncio.run(main())
